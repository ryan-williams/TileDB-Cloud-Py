"""The code to build task graphs for later registration and execution."""

import abc
import uuid
from typing import (
    AbstractSet,
    Any,
    Dict,
    Generic,
    Iterable,
    Optional,
    Set,
    TypeVar,
    Union,
)

import attrs

from tiledb.cloud import utils
from tiledb.cloud._common import ordered
from tiledb.cloud._common import visitor
from tiledb.cloud.taskgraphs import _codec
from tiledb.cloud.taskgraphs import depgraph
from tiledb.cloud.taskgraphs import types

_T = TypeVar("_T")
"""A generic type."""
ValOrNode = Union[_T, "Node[_T]"]
"""Type indicating that you can pass either a direct value or an input node."""
ValOrNodeSeq = Union[
    ValOrNode[types.NativeSequence[_T]],
    types.NativeSequence[ValOrNode[_T]],
]
"""Either a Node that yields a sequence or a sequence that may contain nodes."""

_NOTHING: Any = attrs.make_class("Nothing", (), frozen=True, slots=True)()
"""Sentinel object used when we need to distinguish "unset" from "None"."""


class TaskGraphBuilder:
    """The thing you use to build a task graph.

    This class only *builds* task graphs. The graphs it builds are static and
    only represent the steps to run (the recipe). The actual execution will be
    later performed by the executor.
    """

    def __init__(
        self,
        name: Optional[str] = None,
    ):
        self.name = name
        """A name for this graph. Read-only."""
        self._by_id: Dict[uuid.UUID, Node] = {}
        """The nodes in the graph."""
        self._by_name: Dict[str, Node] = {}
        """The named nodes in the graph, by name."""
        self._deps = depgraph.DepGraph[Node]()
        """A mapping from child to set of parents."""

    def array_read(
        self,
        uri: ValOrNode[str],
        *,
        # TODO: Support query layout.
        raw_ranges: Optional[ValOrNodeSeq[Any]] = None,
        buffers: Optional[ValOrNodeSeq[str]] = None,
        name: Optional[str] = None,
    ) -> "Node[types.ArrayMultiIndex]":
        """Creates a Node that will read data from a TileDB array.

        This Node is not executed immediately; instead, it is used in the same
        way as the array input to an Array UDF works: when an actual UDF is
        executed, the array is queried server-side and is passed as a parameter
        to the user code.

        :param uri: The URI to query against. This must be a ``tiledb://`` URI.
            May be provided either as the URI itself, or as the output
            of an upstream node.

        :param raw_ranges: The ranges to query against. This is called "raw"
            because we accept the format that is passed to the server::

                [
                    [startDim1A, endDim1A, startDim1B, endDim1B, ...],
                    [startDim2A, endDim2A, startDim2B, endDim2B, ...],
                ]

            This may also be provided as either a value or a Node output.

        :param buffers: Optionally, the buffers to query against.
            May be either a raw value or the Node output.

        :param name: An optional name for this Node.
        """
        return self._add_node(_ArrayNode(uri, raw_ranges, buffers, name=name))

    def input(
        self,
        name: str,
        default_value: _T = _NOTHING,
    ) -> "Node[_T]":
        """Creates a Node that can be used as an input to the graph.

        :param name: The name of this input. Required, since it is used
            when executing to match the input to the Node.

        :param default_value: An optional default value to use when executing.
            If not provided, the caller is required to set this input
            when running the task graph.
        """
        return self._add_node(_InputNode(name, default_value))

    def udf(
        self,
        func: utils.Funcable[_T],
        args: types.Arguments = types.Arguments(),
        *,
        result_format: Optional[str] = "python_pickle",
        include_source: bool = True,
        image_name: Optional[str] = None,
        timeout_secs: Optional[int] = None,
        resource_class: Optional[str] = None,
        name: Optional[str] = None,
    ) -> "Node[_T]":
        """Creates a Node which executes a UDF.

        :param func: The function to call; either a Python callable or a
            registered UDF name.
        :param args: The arguments to pass to this function. These may contain
            values or Nodes.
        :param result_format: The format to return results in.
        :param include_source: True (the default) to include the function source
            in the request. This is useful for debugging and logging, but does
            not have any impact on the UDF’s execution. False to omit source.
        :param image_name: If specified, will execute the UDF within
            the specified image rather than the default image for its language.
        :param timeout_secs: If specified, the number of seconds after which
            the UDF will be terminated on the server side. If zero or unset,
            the UDF will run until the server’s configured maximum.Unlike the
            ``timeout`` parameter to Future-like objects, this sets a limit on
            actual execution time, rather than just a limit on how long to wait.
        :param resource_class: If specified, the container resource class
            that this UDF will be executed in.
        """
        # NOTE: When adding parameters here, also update delayed/_udf.py.
        return self._add_node(
            _UDFNode(
                func,
                args,
                include_source=include_source,
                result_format=result_format,
                image_name=image_name,
                timeout_secs=timeout_secs,
                resource_class=resource_class,
                name=name,
            )
        )

    # TODO: array_udf -- a combination of udf and array_read

    def sql(
        self,
        query: str,
        init_commands: Iterable[str] = (),
        parameters: ValOrNodeSeq = (),
        *,
        result_format: str = "arrow",
        name: Optional[str] = None,
    ) -> "Node":
        """Creates a Node that executes an SQL query.

        :param query: The query to execute. This must be a string, and cannot be
            the output of a previous node.
        :param init_commands: A list of SQL commands to execute in the session
            before running ``query``.
        :param parameters: A sequence of objects to provide as parameters for
            the ``?`` placeholders in the ``query``. These may be provided
            either as values or as the output of earlier Nodes.
        :param result_format: The format to provide results in. Either ``json``
            or ``arrow``.
        """
        return self._add_node(
            _SQLNode(
                query,
                init_commands,
                parameters,
                result_format=result_format,
                name=name,
            )
        )

    def add_dep(self, *, parent: "Node", child: "Node") -> None:
        """Manually requires that the ``parent`` must happen before ``child``.

        This should rarely be necessary; including a parent node within
        the parameter list of a child node automatically adds a dependency.
        """
        self._deps.add_edge(child=child, parent=parent)

    def _add_node(self, node: "Node") -> "Node":
        self._deps.add_new_node(node, node.deps)
        self._by_id[node.id] = node
        if node.name is not None:
            if self._by_name.setdefault(node.name, node) is not node:
                self._deps.remove(node)
                raise ValueError(f"A node named {node.name!r} already exists.")

        return node

    def _tdb_to_json(self):
        """Converts this task graph to a registerable/executable format."""
        nodes = self._deps.topo_sorted
        # We need to guarantee that the existing node names are maintained.
        existing_names = set(self._by_name)
        node_jsons = [n.to_registration_json(existing_names) for n in nodes]
        for n, n_json in zip(nodes, node_jsons):
            n_json["depends_on"] = [
                str(parent.id) for parent in self._deps.parents_of(n)
            ]
        return dict(
            name=self.name,
            nodes=node_jsons,
        )


class Node(_codec.TDBJSONEncodable, Generic[_T]):
    """The root type of a Node when building a task graph.

    The basic building block of a task graph. Nodes represent the data and
    execution steps within a TileDB task graph.

    ``builder.Node``s themselves are inert; they only represent the steps that
    will be taken by an Executor implementation to run the task graph. They
    should be treated as opaque and immutable; the Executor's node objects
    are the ones that can be interacted with to get status and results.
    """

    def __init__(
        self,
        name: Optional[str],
        deps: Iterable["Node"],
        *,
        fallback_name: Optional[str] = None,
    ):
        self.id = uuid.uuid4()
        """A unique ID for this node."""
        self.name = name
        """The name of the node. If present, the node is unnamed."""
        self.deps: AbstractSet[Node] = ordered.FrozenSet(deps)
        """The nodes that this node depends upon directly."""
        self._fallback_name = fallback_name or type(self).__name__
        """A string to use to generate a display name if the node is unnamed."""

    @property
    def display_name(self) -> str:
        """A friendly name for the Node."""
        if self.name is not None:
            return self.name
        id_clip = str(self.id)[-12:]
        return f"{self._fallback_name} ({id_clip})"

    def __repr__(self):
        return f"<{type(self).__name__} {self.display_name}>"

    def _tdb_to_json(self) -> types.RegisteredArg:
        """Converts this to the format that will be used in parameter lists.

        This is used when a Node is used as an input to another Node::

            child = dag.udf(..., types.args(parent_node))
        """
        return {
            "__tdbudf__": "node_output",
            "client_node_id": str(self.id),
        }

    @abc.abstractmethod
    def to_registration_json(self, existing_names: Set[str]) -> Dict[str, Any]:
        """Converts this node to the form used when registering the graph.

        This is the form of the Node that will be used to represent it in the
        ``RegisteredTaskGraph`` object, i.e. a ``RegisteredTaskGraphNode``.

        :param existing_names: The set of names that have already been used,
            so that we don't generate a duplicate node name.
        """
        return {
            "client_node_id": str(self.id),
            "name": self._registration_name(existing_names),
        }

    def _registration_name(self, existing: Set[str]) -> str:
        """Generates the unique name to be used when building the graph.

        If the node has a ``name``, then that is used. If not, then it generates
        a new unique name that is not contained within the ``existing`` set,
        and adds that newly-generated name to the set so subsequent Nodes don't
        reuse that name.
        """
        if self.name is not None:
            # A Node which already has a Name does not need to have one generated.
            return self.name
        try:
            return _set_add(existing, self._fallback_name)
        except KeyError:
            pass  # Already present; we gotta try something new.
        id_to_use = self.id
        while True:
            id_str = str(id_to_use)
            for chars in range(2, 13, 2):
                # Try to generate unique names with increasingly large slices
                # of the node's UUID.
                end = id_str[-chars:]
                try:
                    return _set_add(existing, f"{self._fallback_name} ({end})")
                except KeyError:
                    pass  # Sigh, give it more.
            # At this point every single alternate generated name we could generate,
            # from "name (xx)" to "name (xxxxxxxxxxxx)", has been taken.
            # Just throw in a new ID to start from.
            id_to_use = uuid.uuid4()


class _ArrayNode(Node[types.ArrayMultiIndex]):
    """A virutal node representing a query against a TileDB array.

    When used as a parameter to a downstream Node, this will instruct the server
    to execute a query against the given Array and pass that value as the
    parameter to the UDF.
    """

    def __init__(
        self,
        uri: ValOrNode[str],
        raw_ranges: Optional[ValOrNodeSeq[Any]],
        buffers: Optional[ValOrNodeSeq[str]],
        name: Optional[str],
    ):
        """Initializes an ``_ArrayNode``.

        :param uri: The URI to query against. This must be a ``tiledb://`` URI.
            May be provided either as the URI itself, or as the output
            of an upstream node.

        :param raw_ranges: The ranges to query against. This is called "raw"
            because we accept the format that is passed to the server::

                [
                    [startDim1A, endDim1A, startDim1B, endDim1B, ...],
                    [startDim2A, endDim2A, startDim2B, endDim2B, ...],
                ]

            This may also be provided as either a value or a Node output.

        :param buffers: Optionally, the buffers to query against.
            May be either a raw value or the Node output.

        :param name: An optional name for this Node.
        """
        # Currently, the format of ranges we accept here is the raw
        # [[startA1, endA1, startA2, endA2], [startB1, endB1, ...], ...]
        # format. TODO: Figure out how to reliably encode ranges.
        jsoner = _ParameterEscaper()
        self.uri = jsoner.visit(uri)
        self.raw_ranges = jsoner.visit(raw_ranges)
        self.buffers = jsoner.visit(buffers)

        super().__init__(name, jsoner.seen_nodes, fallback_name=f"Query {uri}")

    def to_registration_json(self, existing_names: Set[str]) -> Dict[str, Any]:
        ret = super().to_registration_json(existing_names)
        node_data = dict(
            uri=self.uri,
            ranges={"ranges": self.raw_ranges},
        )
        if self.buffers is not None:
            node_data["buffers"] = self.buffers
        ret["array_node"] = node_data
        return ret


class _InputNode(Node[_T]):
    """An input Node to a task graph that can be specified at execution time."""

    def __init__(self, name: str, default_value: _T):
        """Initializes an input Node.

        :param name: The name of this input. Required, since it is used
            when executing to match the input to the Node.

        :param default_value: An optional default value to use when executing.
            If not provided, the caller is required to set this input
            when running the task graph.
        """
        super().__init__(name, ())
        if default_value is _NOTHING:
            self.default_value = _NOTHING
        else:
            node_finder = _ParameterEscaper()
            self.default_value = node_finder.visit(default_value)
            if node_finder.seen_nodes:
                raise ValueError(
                    "Input nodes cannot have node outputs as default values."
                )

    def to_registration_json(self, existing_names: Set[str]) -> Dict[str, Any]:
        ret = super().to_registration_json(existing_names)
        input_node = {}
        if self.default_value is not _NOTHING:
            input_node["default_value"] = self.default_value
        ret["input_node"] = input_node
        return ret


class _SQLNode(Node):
    """A Node that performs a TileDB Cloud SQL query."""

    def __init__(
        self,
        query: str,
        init_commands: Iterable[str],
        parameters: ValOrNodeSeq,
        *,
        result_format: str,
        name: Optional[str],
    ):
        """Initializes this Node.

        :param query: The query to execute. This must be a string, and cannot be
            the output of a previous node.
        :param init_commands: A list of SQL commands to execute in the session
            before running ``query``.
        :param parameters: A sequence of objects to provide as parameters for
            the ``?`` placeholders in the ``query``. These may be provided
            either as values or as the output of earlier Nodes.
        :param result_format: The format to provide results in. Either ``json``
            or ``arrow``.
        """
        self.query = query
        self.init_commands = tuple(init_commands)
        self.result_format = result_format
        jsoner = _ParameterEscaper()
        self.parameters = jsoner.visit(parameters)
        super().__init__(name, jsoner.seen_nodes, fallback_name="SQL query")

    def to_registration_json(self, existing_names: Set[str]) -> Dict[str, Any]:
        ret = super().to_registration_json(existing_names)
        ret["sql_node"] = dict(
            init_commands=self.init_commands,
            query=self.query,
            parameters=self.parameters,
            result_format=self.result_format,
        )
        return ret


class _UDFNode(Node[_T]):
    """The classic node: the execution of a UDF."""

    def __init__(
        self,
        func: utils.Funcable[_T],
        args: types.Arguments,
        *,
        result_format: Optional[str],
        include_source: bool,
        image_name: Optional[str],
        timeout_secs: Optional[int],
        resource_class: Optional[str],
        name: Optional[str],
    ):
        """Initializes this UDF node.

        See :meth:`TaskGraphBuilder.udf` for details.
        """
        utils.check_funcable(func=func)
        jsoner = _ParameterEscaper()
        self.args = jsoner.arguments_to_json(args)
        super().__init__(
            name,
            jsoner.seen_nodes,
            fallback_name=utils.func_name(func),
        )
        self.func = func
        self.result_format = result_format
        self.include_source = include_source
        self.image_name = image_name
        self.timeout_secs = timeout_secs
        self.resource_class = resource_class

    def to_registration_json(self, existing_names: Set[str]) -> Dict[str, Any]:
        ret = super().to_registration_json(existing_names)
        env_dict = {
            k: v
            for k, v in (
                ("image_name", self.image_name),
                ("timeout", self.timeout_secs),
                ("resource_class", self.resource_class),
            )
            if v
        }
        udf_node = {"arguments": self.args}
        if isinstance(self.func, str):
            udf_node["registered_udf_name"] = self.func
        else:
            env_dict.update(
                language="python",
                language_version=utils.PYTHON_VERSION,
            )
            udf_node["executable_code"] = _codec.b64_str(_codec.pickle(self.func))
            if self.include_source:
                source = utils.getsourcelines(self.func)
                if source:
                    udf_node["source_text"] = source
        if self.result_format:
            udf_node["result_format"] = self.result_format
        udf_node["environment"] = env_dict
        ret["udf_node"] = udf_node
        return ret


class _ParameterEscaper(_codec.Escaper):
    """Converts Python arguments passed into Nodes into serializable format.

    The input to this ``Escaper`` is a ``NativeValue``, i.e. any Python value.
    The output is a ``RegisteredArg``, used to serialize the Node's arguments
    for registration or passing to an Executor.
    """

    def __init__(self):
        super().__init__()
        self.seen_nodes = ordered.Set[Node]()
        """The Nodes we have found when visiting our input(s)."""

    def maybe_replace(self, arg) -> Optional[visitor.Replacement]:
        if isinstance(arg, Node):
            self.seen_nodes.add(arg)
        return super().maybe_replace(arg)

    def arguments_to_json(self, arg: types.Arguments) -> types.RegisteredArg:
        arg_outputs = [{"value": self.visit(val)} for val in arg.args]
        kwarg_outputs = [
            {"name": name, "value": self.visit(value)}
            for (name, value) in arg.kwargs.items()
        ]
        return arg_outputs + kwarg_outputs


def _set_add(s: Set[_T], elem: _T) -> _T:
    """Adds an element to a set, but only if it was missing before."""
    if elem in s:
        raise KeyError(elem)
    s.add(elem)
    return elem
