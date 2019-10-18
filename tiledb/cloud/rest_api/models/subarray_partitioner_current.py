# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.2.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SubarrayPartitionerCurrent(object):
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
        'subarray': 'Subarray',
        'start': 'int',
        'end': 'int',
        'split_multi_range': 'bool'
    }

    attribute_map = {
        'subarray': 'subarray',
        'start': 'start',
        'end': 'end',
        'split_multi_range': 'splitMultiRange'
    }

    def __init__(self, subarray=None, start=None, end=None, split_multi_range=None):  # noqa: E501
        """SubarrayPartitionerCurrent - a model defined in OpenAPI"""  # noqa: E501

        self._subarray = None
        self._start = None
        self._end = None
        self._split_multi_range = None
        self.discriminator = None

        if subarray is not None:
            self.subarray = subarray
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if split_multi_range is not None:
            self.split_multi_range = split_multi_range

    @property
    def subarray(self):
        """Gets the subarray of this SubarrayPartitionerCurrent.  # noqa: E501


        :return: The subarray of this SubarrayPartitionerCurrent.  # noqa: E501
        :rtype: Subarray
        """
        return self._subarray

    @subarray.setter
    def subarray(self, subarray):
        """Sets the subarray of this SubarrayPartitionerCurrent.


        :param subarray: The subarray of this SubarrayPartitionerCurrent.  # noqa: E501
        :type: Subarray
        """

        self._subarray = subarray

    @property
    def start(self):
        """Gets the start of this SubarrayPartitionerCurrent.  # noqa: E501

        PartitionInfo start  # noqa: E501

        :return: The start of this SubarrayPartitionerCurrent.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SubarrayPartitionerCurrent.

        PartitionInfo start  # noqa: E501

        :param start: The start of this SubarrayPartitionerCurrent.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this SubarrayPartitionerCurrent.  # noqa: E501

        PartitionInfo end  # noqa: E501

        :return: The end of this SubarrayPartitionerCurrent.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SubarrayPartitionerCurrent.

        PartitionInfo end  # noqa: E501

        :param end: The end of this SubarrayPartitionerCurrent.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def split_multi_range(self):
        """Gets the split_multi_range of this SubarrayPartitionerCurrent.  # noqa: E501

        PartitionInfo splitMultiRange  # noqa: E501

        :return: The split_multi_range of this SubarrayPartitionerCurrent.  # noqa: E501
        :rtype: bool
        """
        return self._split_multi_range

    @split_multi_range.setter
    def split_multi_range(self, split_multi_range):
        """Sets the split_multi_range of this SubarrayPartitionerCurrent.

        PartitionInfo splitMultiRange  # noqa: E501

        :param split_multi_range: The split_multi_range of this SubarrayPartitionerCurrent.  # noqa: E501
        :type: bool
        """

        self._split_multi_range = split_multi_range

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, SubarrayPartitionerCurrent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
