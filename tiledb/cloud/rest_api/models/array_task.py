# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ArrayTask(object):
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
        "id": "str",
        "name": "str",
        "description": "str",
        "array_metadata": "ArrayInfo",
        "subarray": "DomainArray",
        "memory": "int",
        "cpu": "int",
        "namespace": "str",
        "status": "ArrayTaskStatus",
        "start_time": "datetime",
        "finish_time": "datetime",
        "cost": "int",
        "query_type": "Querytype",
        "udf_code": "str",
        "udf_language": "str",
        "sql_query": "str",
        "type": "ArrayTaskType",
        "activity": "list[ArrayActivityLog]",
        "logs": "str",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "description": "description",
        "array_metadata": "array_metadata",
        "subarray": "subarray",
        "memory": "memory",
        "cpu": "cpu",
        "namespace": "namespace",
        "status": "status",
        "start_time": "start_time",
        "finish_time": "finish_time",
        "cost": "cost",
        "query_type": "query_type",
        "udf_code": "udf_code",
        "udf_language": "udf_language",
        "sql_query": "sql_query",
        "type": "type",
        "activity": "activity",
        "logs": "logs",
    }

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        array_metadata=None,
        subarray=None,
        memory=None,
        cpu=None,
        namespace=None,
        status=None,
        start_time=None,
        finish_time=None,
        cost=None,
        query_type=None,
        udf_code=None,
        udf_language=None,
        sql_query=None,
        type=None,
        activity=None,
        logs=None,
    ):  # noqa: E501
        """ArrayTask - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._array_metadata = None
        self._subarray = None
        self._memory = None
        self._cpu = None
        self._namespace = None
        self._status = None
        self._start_time = None
        self._finish_time = None
        self._cost = None
        self._query_type = None
        self._udf_code = None
        self._udf_language = None
        self._sql_query = None
        self._type = None
        self._activity = None
        self._logs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if array_metadata is not None:
            self.array_metadata = array_metadata
        if subarray is not None:
            self.subarray = subarray
        if memory is not None:
            self.memory = memory
        if cpu is not None:
            self.cpu = cpu
        if namespace is not None:
            self.namespace = namespace
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if cost is not None:
            self.cost = cost
        if query_type is not None:
            self.query_type = query_type
        if udf_code is not None:
            self.udf_code = udf_code
        if udf_language is not None:
            self.udf_language = udf_language
        if sql_query is not None:
            self.sql_query = sql_query
        if type is not None:
            self.type = type
        if activity is not None:
            self.activity = activity
        if logs is not None:
            self.logs = logs

    @property
    def id(self):
        """Gets the id of this ArrayTask.  # noqa: E501

        task id  # noqa: E501

        :return: The id of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArrayTask.

        task id  # noqa: E501

        :param id: The id of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ArrayTask.  # noqa: E501

        Optional task name  # noqa: E501

        :return: The name of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArrayTask.

        Optional task name  # noqa: E501

        :param name: The name of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ArrayTask.  # noqa: E501

        Optional task description (Tasks purpose)  # noqa: E501

        :return: The description of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArrayTask.

        Optional task description (Tasks purpose)  # noqa: E501

        :param description: The description of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def array_metadata(self):
        """Gets the array_metadata of this ArrayTask.  # noqa: E501


        :return: The array_metadata of this ArrayTask.  # noqa: E501
        :rtype: ArrayInfo
        """
        return self._array_metadata

    @array_metadata.setter
    def array_metadata(self, array_metadata):
        """Sets the array_metadata of this ArrayTask.


        :param array_metadata: The array_metadata of this ArrayTask.  # noqa: E501
        :type: ArrayInfo
        """

        self._array_metadata = array_metadata

    @property
    def subarray(self):
        """Gets the subarray of this ArrayTask.  # noqa: E501


        :return: The subarray of this ArrayTask.  # noqa: E501
        :rtype: DomainArray
        """
        return self._subarray

    @subarray.setter
    def subarray(self, subarray):
        """Sets the subarray of this ArrayTask.


        :param subarray: The subarray of this ArrayTask.  # noqa: E501
        :type: DomainArray
        """

        self._subarray = subarray

    @property
    def memory(self):
        """Gets the memory of this ArrayTask.  # noqa: E501

        memory allocated to task in bytes  # noqa: E501

        :return: The memory of this ArrayTask.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ArrayTask.

        memory allocated to task in bytes  # noqa: E501

        :param memory: The memory of this ArrayTask.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this ArrayTask.  # noqa: E501

        millicpu allocated to task  # noqa: E501

        :return: The cpu of this ArrayTask.  # noqa: E501
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ArrayTask.

        millicpu allocated to task  # noqa: E501

        :param cpu: The cpu of this ArrayTask.  # noqa: E501
        :type: int
        """

        self._cpu = cpu

    @property
    def namespace(self):
        """Gets the namespace of this ArrayTask.  # noqa: E501

        namespace task is tied to  # noqa: E501

        :return: The namespace of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ArrayTask.

        namespace task is tied to  # noqa: E501

        :param namespace: The namespace of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def status(self):
        """Gets the status of this ArrayTask.  # noqa: E501


        :return: The status of this ArrayTask.  # noqa: E501
        :rtype: ArrayTaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ArrayTask.


        :param status: The status of this ArrayTask.  # noqa: E501
        :type: ArrayTaskStatus
        """

        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ArrayTask.  # noqa: E501

        Start time RFC3339 for job  # noqa: E501

        :return: The start_time of this ArrayTask.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ArrayTask.

        Start time RFC3339 for job  # noqa: E501

        :param start_time: The start_time of this ArrayTask.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def finish_time(self):
        """Gets the finish_time of this ArrayTask.  # noqa: E501

        Finish time RFC3339 for job  # noqa: E501

        :return: The finish_time of this ArrayTask.  # noqa: E501
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this ArrayTask.

        Finish time RFC3339 for job  # noqa: E501

        :param finish_time: The finish_time of this ArrayTask.  # noqa: E501
        :type: datetime
        """

        self._finish_time = finish_time

    @property
    def cost(self):
        """Gets the cost of this ArrayTask.  # noqa: E501

        Cost accumulated for task in 0.01 USD, example is 1 USD  # noqa: E501

        :return: The cost of this ArrayTask.  # noqa: E501
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ArrayTask.

        Cost accumulated for task in 0.01 USD, example is 1 USD  # noqa: E501

        :param cost: The cost of this ArrayTask.  # noqa: E501
        :type: int
        """

        self._cost = cost

    @property
    def query_type(self):
        """Gets the query_type of this ArrayTask.  # noqa: E501


        :return: The query_type of this ArrayTask.  # noqa: E501
        :rtype: Querytype
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ArrayTask.


        :param query_type: The query_type of this ArrayTask.  # noqa: E501
        :type: Querytype
        """

        self._query_type = query_type

    @property
    def udf_code(self):
        """Gets the udf_code of this ArrayTask.  # noqa: E501

        Optional actual code that is going to be executed  # noqa: E501

        :return: The udf_code of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._udf_code

    @udf_code.setter
    def udf_code(self, udf_code):
        """Sets the udf_code of this ArrayTask.

        Optional actual code that is going to be executed  # noqa: E501

        :param udf_code: The udf_code of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._udf_code = udf_code

    @property
    def udf_language(self):
        """Gets the udf_language of this ArrayTask.  # noqa: E501

        Optional actual language used to express udf_code  # noqa: E501

        :return: The udf_language of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._udf_language

    @udf_language.setter
    def udf_language(self, udf_language):
        """Sets the udf_language of this ArrayTask.

        Optional actual language used to express udf_code  # noqa: E501

        :param udf_language: The udf_language of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._udf_language = udf_language

    @property
    def sql_query(self):
        """Gets the sql_query of this ArrayTask.  # noqa: E501

        Optional actual sql query that is going to be executed  # noqa: E501

        :return: The sql_query of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._sql_query

    @sql_query.setter
    def sql_query(self, sql_query):
        """Sets the sql_query of this ArrayTask.

        Optional actual sql query that is going to be executed  # noqa: E501

        :param sql_query: The sql_query of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._sql_query = sql_query

    @property
    def type(self):
        """Gets the type of this ArrayTask.  # noqa: E501


        :return: The type of this ArrayTask.  # noqa: E501
        :rtype: ArrayTaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ArrayTask.


        :param type: The type of this ArrayTask.  # noqa: E501
        :type: ArrayTaskType
        """

        self._type = type

    @property
    def activity(self):
        """Gets the activity of this ArrayTask.  # noqa: E501

        Array activity logs for task  # noqa: E501

        :return: The activity of this ArrayTask.  # noqa: E501
        :rtype: list[ArrayActivityLog]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ArrayTask.

        Array activity logs for task  # noqa: E501

        :param activity: The activity of this ArrayTask.  # noqa: E501
        :type: list[ArrayActivityLog]
        """

        self._activity = activity

    @property
    def logs(self):
        """Gets the logs of this ArrayTask.  # noqa: E501

        logs from array task  # noqa: E501

        :return: The logs of this ArrayTask.  # noqa: E501
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ArrayTask.

        logs from array task  # noqa: E501

        :param logs: The logs of this ArrayTask.  # noqa: E501
        :type: str
        """

        self._logs = logs

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
        if not isinstance(other, ArrayTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
