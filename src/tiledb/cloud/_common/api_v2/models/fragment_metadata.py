# coding: utf-8

"""
    Tiledb Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tiledb.cloud._common.api_v2.configuration import Configuration


class FragmentMetadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "file_sizes": "list[float]",
        "file_var_sizes": "list[float]",
        "file_validity_sizes": "list[float]",
        "fragment_uri": "str",
        "has_timestamps": "bool",
        "has_delete_meta": "bool",
        "sparse_tile_num": "float",
        "tile_index_base": "float",
        "tile_offsets": "list[list[float]]",
        "tile_var_offsets": "list[list[float]]",
        "tile_var_sizes": "list[list[float]]",
        "tile_validity_offsets": "list[list[float]]",
        "tile_min_buffer": "list[list[float]]",
        "tile_min_var_buffer": "list[list[float]]",
        "tile_max_buffer": "list[list[float]]",
        "tile_max_var_buffer": "list[list[float]]",
        "tile_sums": "list[list[float]]",
        "tile_null_counts": "list[list[float]]",
        "fragment_mins": "list[list[float]]",
        "fragment_maxs": "list[list[float]]",
        "fragment_sums": "list[float]",
        "fragment_null_counts": "list[float]",
        "version": "int",
        "timestamp_range": "list[float]",
        "last_tile_cell_num": "int",
        "non_empty_domain": "NonEmptyDomainList",
        "rtree": "file",
        "has_consolidated_footer": "bool",
        "gt_offsets": "GenericTileOffsets",
    }

    attribute_map = {
        "file_sizes": "fileSizes",
        "file_var_sizes": "fileVarSizes",
        "file_validity_sizes": "fileValiditySizes",
        "fragment_uri": "fragmentUri",
        "has_timestamps": "hasTimestamps",
        "has_delete_meta": "hasDeleteMeta",
        "sparse_tile_num": "sparseTileNum",
        "tile_index_base": "tileIndexBase",
        "tile_offsets": "tileOffsets",
        "tile_var_offsets": "tileVarOffsets",
        "tile_var_sizes": "tileVarSizes",
        "tile_validity_offsets": "tileValidityOffsets",
        "tile_min_buffer": "tileMinBuffer",
        "tile_min_var_buffer": "tileMinVarBuffer",
        "tile_max_buffer": "tileMaxBuffer",
        "tile_max_var_buffer": "tileMaxVarBuffer",
        "tile_sums": "tileSums",
        "tile_null_counts": "tileNullCounts",
        "fragment_mins": "fragmentMins",
        "fragment_maxs": "fragmentMaxs",
        "fragment_sums": "fragmentSums",
        "fragment_null_counts": "fragmentNullCounts",
        "version": "version",
        "timestamp_range": "timestampRange",
        "last_tile_cell_num": "lastTileCellNum",
        "non_empty_domain": "nonEmptyDomain",
        "rtree": "rtree",
        "has_consolidated_footer": "hasConsolidatedFooter",
        "gt_offsets": "gtOffsets",
    }

    def __init__(
        self,
        file_sizes=None,
        file_var_sizes=None,
        file_validity_sizes=None,
        fragment_uri=None,
        has_timestamps=None,
        has_delete_meta=None,
        sparse_tile_num=None,
        tile_index_base=None,
        tile_offsets=None,
        tile_var_offsets=None,
        tile_var_sizes=None,
        tile_validity_offsets=None,
        tile_min_buffer=None,
        tile_min_var_buffer=None,
        tile_max_buffer=None,
        tile_max_var_buffer=None,
        tile_sums=None,
        tile_null_counts=None,
        fragment_mins=None,
        fragment_maxs=None,
        fragment_sums=None,
        fragment_null_counts=None,
        version=None,
        timestamp_range=None,
        last_tile_cell_num=None,
        non_empty_domain=None,
        rtree=None,
        has_consolidated_footer=None,
        gt_offsets=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """FragmentMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_sizes = None
        self._file_var_sizes = None
        self._file_validity_sizes = None
        self._fragment_uri = None
        self._has_timestamps = None
        self._has_delete_meta = None
        self._sparse_tile_num = None
        self._tile_index_base = None
        self._tile_offsets = None
        self._tile_var_offsets = None
        self._tile_var_sizes = None
        self._tile_validity_offsets = None
        self._tile_min_buffer = None
        self._tile_min_var_buffer = None
        self._tile_max_buffer = None
        self._tile_max_var_buffer = None
        self._tile_sums = None
        self._tile_null_counts = None
        self._fragment_mins = None
        self._fragment_maxs = None
        self._fragment_sums = None
        self._fragment_null_counts = None
        self._version = None
        self._timestamp_range = None
        self._last_tile_cell_num = None
        self._non_empty_domain = None
        self._rtree = None
        self._has_consolidated_footer = None
        self._gt_offsets = None
        self.discriminator = None

        if file_sizes is not None:
            self.file_sizes = file_sizes
        if file_var_sizes is not None:
            self.file_var_sizes = file_var_sizes
        if file_validity_sizes is not None:
            self.file_validity_sizes = file_validity_sizes
        if fragment_uri is not None:
            self.fragment_uri = fragment_uri
        if has_timestamps is not None:
            self.has_timestamps = has_timestamps
        if has_delete_meta is not None:
            self.has_delete_meta = has_delete_meta
        if sparse_tile_num is not None:
            self.sparse_tile_num = sparse_tile_num
        if tile_index_base is not None:
            self.tile_index_base = tile_index_base
        if tile_offsets is not None:
            self.tile_offsets = tile_offsets
        if tile_var_offsets is not None:
            self.tile_var_offsets = tile_var_offsets
        if tile_var_sizes is not None:
            self.tile_var_sizes = tile_var_sizes
        if tile_validity_offsets is not None:
            self.tile_validity_offsets = tile_validity_offsets
        if tile_min_buffer is not None:
            self.tile_min_buffer = tile_min_buffer
        if tile_min_var_buffer is not None:
            self.tile_min_var_buffer = tile_min_var_buffer
        if tile_max_buffer is not None:
            self.tile_max_buffer = tile_max_buffer
        if tile_max_var_buffer is not None:
            self.tile_max_var_buffer = tile_max_var_buffer
        if tile_sums is not None:
            self.tile_sums = tile_sums
        if tile_null_counts is not None:
            self.tile_null_counts = tile_null_counts
        if fragment_mins is not None:
            self.fragment_mins = fragment_mins
        if fragment_maxs is not None:
            self.fragment_maxs = fragment_maxs
        if fragment_sums is not None:
            self.fragment_sums = fragment_sums
        if fragment_null_counts is not None:
            self.fragment_null_counts = fragment_null_counts
        if version is not None:
            self.version = version
        if timestamp_range is not None:
            self.timestamp_range = timestamp_range
        if last_tile_cell_num is not None:
            self.last_tile_cell_num = last_tile_cell_num
        if non_empty_domain is not None:
            self.non_empty_domain = non_empty_domain
        if rtree is not None:
            self.rtree = rtree
        if has_consolidated_footer is not None:
            self.has_consolidated_footer = has_consolidated_footer
        if gt_offsets is not None:
            self.gt_offsets = gt_offsets

    @property
    def file_sizes(self):
        """Gets the file_sizes of this FragmentMetadata.  # noqa: E501

        The size of each attribute file  # noqa: E501

        :return: The file_sizes of this FragmentMetadata.  # noqa: E501
        :rtype: list[float]
        """
        return self._file_sizes

    @file_sizes.setter
    def file_sizes(self, file_sizes):
        """Sets the file_sizes of this FragmentMetadata.

        The size of each attribute file  # noqa: E501

        :param file_sizes: The file_sizes of this FragmentMetadata.  # noqa: E501
        :type: list[float]
        """

        self._file_sizes = file_sizes

    @property
    def file_var_sizes(self):
        """Gets the file_var_sizes of this FragmentMetadata.  # noqa: E501

        The size of each var attribute file  # noqa: E501

        :return: The file_var_sizes of this FragmentMetadata.  # noqa: E501
        :rtype: list[float]
        """
        return self._file_var_sizes

    @file_var_sizes.setter
    def file_var_sizes(self, file_var_sizes):
        """Sets the file_var_sizes of this FragmentMetadata.

        The size of each var attribute file  # noqa: E501

        :param file_var_sizes: The file_var_sizes of this FragmentMetadata.  # noqa: E501
        :type: list[float]
        """

        self._file_var_sizes = file_var_sizes

    @property
    def file_validity_sizes(self):
        """Gets the file_validity_sizes of this FragmentMetadata.  # noqa: E501

        The size of each validity attribute file  # noqa: E501

        :return: The file_validity_sizes of this FragmentMetadata.  # noqa: E501
        :rtype: list[float]
        """
        return self._file_validity_sizes

    @file_validity_sizes.setter
    def file_validity_sizes(self, file_validity_sizes):
        """Sets the file_validity_sizes of this FragmentMetadata.

        The size of each validity attribute file  # noqa: E501

        :param file_validity_sizes: The file_validity_sizes of this FragmentMetadata.  # noqa: E501
        :type: list[float]
        """

        self._file_validity_sizes = file_validity_sizes

    @property
    def fragment_uri(self):
        """Gets the fragment_uri of this FragmentMetadata.  # noqa: E501

        The uri of the fragment this metadata belongs to  # noqa: E501

        :return: The fragment_uri of this FragmentMetadata.  # noqa: E501
        :rtype: str
        """
        return self._fragment_uri

    @fragment_uri.setter
    def fragment_uri(self, fragment_uri):
        """Sets the fragment_uri of this FragmentMetadata.

        The uri of the fragment this metadata belongs to  # noqa: E501

        :param fragment_uri: The fragment_uri of this FragmentMetadata.  # noqa: E501
        :type: str
        """

        self._fragment_uri = fragment_uri

    @property
    def has_timestamps(self):
        """Gets the has_timestamps of this FragmentMetadata.  # noqa: E501

        True if the fragment has timestamps  # noqa: E501

        :return: The has_timestamps of this FragmentMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._has_timestamps

    @has_timestamps.setter
    def has_timestamps(self, has_timestamps):
        """Sets the has_timestamps of this FragmentMetadata.

        True if the fragment has timestamps  # noqa: E501

        :param has_timestamps: The has_timestamps of this FragmentMetadata.  # noqa: E501
        :type: bool
        """

        self._has_timestamps = has_timestamps

    @property
    def has_delete_meta(self):
        """Gets the has_delete_meta of this FragmentMetadata.  # noqa: E501

        True if the fragment has delete metadata  # noqa: E501

        :return: The has_delete_meta of this FragmentMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._has_delete_meta

    @has_delete_meta.setter
    def has_delete_meta(self, has_delete_meta):
        """Sets the has_delete_meta of this FragmentMetadata.

        True if the fragment has delete metadata  # noqa: E501

        :param has_delete_meta: The has_delete_meta of this FragmentMetadata.  # noqa: E501
        :type: bool
        """

        self._has_delete_meta = has_delete_meta

    @property
    def sparse_tile_num(self):
        """Gets the sparse_tile_num of this FragmentMetadata.  # noqa: E501

        The number of sparse tiles  # noqa: E501

        :return: The sparse_tile_num of this FragmentMetadata.  # noqa: E501
        :rtype: float
        """
        return self._sparse_tile_num

    @sparse_tile_num.setter
    def sparse_tile_num(self, sparse_tile_num):
        """Sets the sparse_tile_num of this FragmentMetadata.

        The number of sparse tiles  # noqa: E501

        :param sparse_tile_num: The sparse_tile_num of this FragmentMetadata.  # noqa: E501
        :type: float
        """

        self._sparse_tile_num = sparse_tile_num

    @property
    def tile_index_base(self):
        """Gets the tile_index_base of this FragmentMetadata.  # noqa: E501

        Used to track the tile index base between global order writes  # noqa: E501

        :return: The tile_index_base of this FragmentMetadata.  # noqa: E501
        :rtype: float
        """
        return self._tile_index_base

    @tile_index_base.setter
    def tile_index_base(self, tile_index_base):
        """Sets the tile_index_base of this FragmentMetadata.

        Used to track the tile index base between global order writes  # noqa: E501

        :param tile_index_base: The tile_index_base of this FragmentMetadata.  # noqa: E501
        :type: float
        """

        self._tile_index_base = tile_index_base

    @property
    def tile_offsets(self):
        """Gets the tile_offsets of this FragmentMetadata.  # noqa: E501

        Tile offsets in their attribute files  # noqa: E501

        :return: The tile_offsets of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_offsets

    @tile_offsets.setter
    def tile_offsets(self, tile_offsets):
        """Sets the tile_offsets of this FragmentMetadata.

        Tile offsets in their attribute files  # noqa: E501

        :param tile_offsets: The tile_offsets of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_offsets = tile_offsets

    @property
    def tile_var_offsets(self):
        """Gets the tile_var_offsets of this FragmentMetadata.  # noqa: E501

        Variable tile offsets in their attribute files  # noqa: E501

        :return: The tile_var_offsets of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_var_offsets

    @tile_var_offsets.setter
    def tile_var_offsets(self, tile_var_offsets):
        """Sets the tile_var_offsets of this FragmentMetadata.

        Variable tile offsets in their attribute files  # noqa: E501

        :param tile_var_offsets: The tile_var_offsets of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_var_offsets = tile_var_offsets

    @property
    def tile_var_sizes(self):
        """Gets the tile_var_sizes of this FragmentMetadata.  # noqa: E501

        The sizes of the uncompressed variable tiles  # noqa: E501

        :return: The tile_var_sizes of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_var_sizes

    @tile_var_sizes.setter
    def tile_var_sizes(self, tile_var_sizes):
        """Sets the tile_var_sizes of this FragmentMetadata.

        The sizes of the uncompressed variable tiles  # noqa: E501

        :param tile_var_sizes: The tile_var_sizes of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_var_sizes = tile_var_sizes

    @property
    def tile_validity_offsets(self):
        """Gets the tile_validity_offsets of this FragmentMetadata.  # noqa: E501

        Validity tile offests in their attribute files  # noqa: E501

        :return: The tile_validity_offsets of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_validity_offsets

    @tile_validity_offsets.setter
    def tile_validity_offsets(self, tile_validity_offsets):
        """Sets the tile_validity_offsets of this FragmentMetadata.

        Validity tile offests in their attribute files  # noqa: E501

        :param tile_validity_offsets: The tile_validity_offsets of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_validity_offsets = tile_validity_offsets

    @property
    def tile_min_buffer(self):
        """Gets the tile_min_buffer of this FragmentMetadata.  # noqa: E501

        tile min buffers  # noqa: E501

        :return: The tile_min_buffer of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_min_buffer

    @tile_min_buffer.setter
    def tile_min_buffer(self, tile_min_buffer):
        """Sets the tile_min_buffer of this FragmentMetadata.

        tile min buffers  # noqa: E501

        :param tile_min_buffer: The tile_min_buffer of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_min_buffer = tile_min_buffer

    @property
    def tile_min_var_buffer(self):
        """Gets the tile_min_var_buffer of this FragmentMetadata.  # noqa: E501

        tile min buffers for var length data  # noqa: E501

        :return: The tile_min_var_buffer of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_min_var_buffer

    @tile_min_var_buffer.setter
    def tile_min_var_buffer(self, tile_min_var_buffer):
        """Sets the tile_min_var_buffer of this FragmentMetadata.

        tile min buffers for var length data  # noqa: E501

        :param tile_min_var_buffer: The tile_min_var_buffer of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_min_var_buffer = tile_min_var_buffer

    @property
    def tile_max_buffer(self):
        """Gets the tile_max_buffer of this FragmentMetadata.  # noqa: E501

        tile max buffers  # noqa: E501

        :return: The tile_max_buffer of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_max_buffer

    @tile_max_buffer.setter
    def tile_max_buffer(self, tile_max_buffer):
        """Sets the tile_max_buffer of this FragmentMetadata.

        tile max buffers  # noqa: E501

        :param tile_max_buffer: The tile_max_buffer of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_max_buffer = tile_max_buffer

    @property
    def tile_max_var_buffer(self):
        """Gets the tile_max_var_buffer of this FragmentMetadata.  # noqa: E501

        tile max buffers for var length data  # noqa: E501

        :return: The tile_max_var_buffer of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_max_var_buffer

    @tile_max_var_buffer.setter
    def tile_max_var_buffer(self, tile_max_var_buffer):
        """Sets the tile_max_var_buffer of this FragmentMetadata.

        tile max buffers for var length data  # noqa: E501

        :param tile_max_var_buffer: The tile_max_var_buffer of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_max_var_buffer = tile_max_var_buffer

    @property
    def tile_sums(self):
        """Gets the tile_sums of this FragmentMetadata.  # noqa: E501

        tile sum values  # noqa: E501

        :return: The tile_sums of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_sums

    @tile_sums.setter
    def tile_sums(self, tile_sums):
        """Sets the tile_sums of this FragmentMetadata.

        tile sum values  # noqa: E501

        :param tile_sums: The tile_sums of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_sums = tile_sums

    @property
    def tile_null_counts(self):
        """Gets the tile_null_counts of this FragmentMetadata.  # noqa: E501

        tile null count values  # noqa: E501

        :return: The tile_null_counts of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._tile_null_counts

    @tile_null_counts.setter
    def tile_null_counts(self, tile_null_counts):
        """Sets the tile_null_counts of this FragmentMetadata.

        tile null count values  # noqa: E501

        :param tile_null_counts: The tile_null_counts of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._tile_null_counts = tile_null_counts

    @property
    def fragment_mins(self):
        """Gets the fragment_mins of this FragmentMetadata.  # noqa: E501

        fragment min values  # noqa: E501

        :return: The fragment_mins of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._fragment_mins

    @fragment_mins.setter
    def fragment_mins(self, fragment_mins):
        """Sets the fragment_mins of this FragmentMetadata.

        fragment min values  # noqa: E501

        :param fragment_mins: The fragment_mins of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._fragment_mins = fragment_mins

    @property
    def fragment_maxs(self):
        """Gets the fragment_maxs of this FragmentMetadata.  # noqa: E501

        fragment max values  # noqa: E501

        :return: The fragment_maxs of this FragmentMetadata.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._fragment_maxs

    @fragment_maxs.setter
    def fragment_maxs(self, fragment_maxs):
        """Sets the fragment_maxs of this FragmentMetadata.

        fragment max values  # noqa: E501

        :param fragment_maxs: The fragment_maxs of this FragmentMetadata.  # noqa: E501
        :type: list[list[float]]
        """

        self._fragment_maxs = fragment_maxs

    @property
    def fragment_sums(self):
        """Gets the fragment_sums of this FragmentMetadata.  # noqa: E501

        fragment sum values  # noqa: E501

        :return: The fragment_sums of this FragmentMetadata.  # noqa: E501
        :rtype: list[float]
        """
        return self._fragment_sums

    @fragment_sums.setter
    def fragment_sums(self, fragment_sums):
        """Sets the fragment_sums of this FragmentMetadata.

        fragment sum values  # noqa: E501

        :param fragment_sums: The fragment_sums of this FragmentMetadata.  # noqa: E501
        :type: list[float]
        """

        self._fragment_sums = fragment_sums

    @property
    def fragment_null_counts(self):
        """Gets the fragment_null_counts of this FragmentMetadata.  # noqa: E501

        fragment null count values  # noqa: E501

        :return: The fragment_null_counts of this FragmentMetadata.  # noqa: E501
        :rtype: list[float]
        """
        return self._fragment_null_counts

    @fragment_null_counts.setter
    def fragment_null_counts(self, fragment_null_counts):
        """Sets the fragment_null_counts of this FragmentMetadata.

        fragment null count values  # noqa: E501

        :param fragment_null_counts: The fragment_null_counts of this FragmentMetadata.  # noqa: E501
        :type: list[float]
        """

        self._fragment_null_counts = fragment_null_counts

    @property
    def version(self):
        """Gets the version of this FragmentMetadata.  # noqa: E501

        the format version of this metadata  # noqa: E501

        :return: The version of this FragmentMetadata.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FragmentMetadata.

        the format version of this metadata  # noqa: E501

        :param version: The version of this FragmentMetadata.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def timestamp_range(self):
        """Gets the timestamp_range of this FragmentMetadata.  # noqa: E501

        A pair of timestamps for fragment  # noqa: E501

        :return: The timestamp_range of this FragmentMetadata.  # noqa: E501
        :rtype: list[float]
        """
        return self._timestamp_range

    @timestamp_range.setter
    def timestamp_range(self, timestamp_range):
        """Sets the timestamp_range of this FragmentMetadata.

        A pair of timestamps for fragment  # noqa: E501

        :param timestamp_range: The timestamp_range of this FragmentMetadata.  # noqa: E501
        :type: list[float]
        """

        self._timestamp_range = timestamp_range

    @property
    def last_tile_cell_num(self):
        """Gets the last_tile_cell_num of this FragmentMetadata.  # noqa: E501

        The number of cells in the last tile  # noqa: E501

        :return: The last_tile_cell_num of this FragmentMetadata.  # noqa: E501
        :rtype: int
        """
        return self._last_tile_cell_num

    @last_tile_cell_num.setter
    def last_tile_cell_num(self, last_tile_cell_num):
        """Sets the last_tile_cell_num of this FragmentMetadata.

        The number of cells in the last tile  # noqa: E501

        :param last_tile_cell_num: The last_tile_cell_num of this FragmentMetadata.  # noqa: E501
        :type: int
        """

        self._last_tile_cell_num = last_tile_cell_num

    @property
    def non_empty_domain(self):
        """Gets the non_empty_domain of this FragmentMetadata.  # noqa: E501


        :return: The non_empty_domain of this FragmentMetadata.  # noqa: E501
        :rtype: NonEmptyDomainList
        """
        return self._non_empty_domain

    @non_empty_domain.setter
    def non_empty_domain(self, non_empty_domain):
        """Sets the non_empty_domain of this FragmentMetadata.


        :param non_empty_domain: The non_empty_domain of this FragmentMetadata.  # noqa: E501
        :type: NonEmptyDomainList
        """

        self._non_empty_domain = non_empty_domain

    @property
    def rtree(self):
        """Gets the rtree of this FragmentMetadata.  # noqa: E501

        The RTree for the MBRs serialized as a blob  # noqa: E501

        :return: The rtree of this FragmentMetadata.  # noqa: E501
        :rtype: file
        """
        return self._rtree

    @rtree.setter
    def rtree(self, rtree):
        """Sets the rtree of this FragmentMetadata.

        The RTree for the MBRs serialized as a blob  # noqa: E501

        :param rtree: The rtree of this FragmentMetadata.  # noqa: E501
        :type: file
        """

        self._rtree = rtree

    @property
    def has_consolidated_footer(self):
        """Gets the has_consolidated_footer of this FragmentMetadata.  # noqa: E501

        if the fragment metadata footer appears in a consolidated file  # noqa: E501

        :return: The has_consolidated_footer of this FragmentMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._has_consolidated_footer

    @has_consolidated_footer.setter
    def has_consolidated_footer(self, has_consolidated_footer):
        """Sets the has_consolidated_footer of this FragmentMetadata.

        if the fragment metadata footer appears in a consolidated file  # noqa: E501

        :param has_consolidated_footer: The has_consolidated_footer of this FragmentMetadata.  # noqa: E501
        :type: bool
        """

        self._has_consolidated_footer = has_consolidated_footer

    @property
    def gt_offsets(self):
        """Gets the gt_offsets of this FragmentMetadata.  # noqa: E501


        :return: The gt_offsets of this FragmentMetadata.  # noqa: E501
        :rtype: GenericTileOffsets
        """
        return self._gt_offsets

    @gt_offsets.setter
    def gt_offsets(self, gt_offsets):
        """Sets the gt_offsets of this FragmentMetadata.


        :param gt_offsets: The gt_offsets of this FragmentMetadata.  # noqa: E501
        :type: GenericTileOffsets
        """

        self._gt_offsets = gt_offsets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FragmentMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FragmentMetadata):
            return True

        return self.to_dict() != other.to_dict()
