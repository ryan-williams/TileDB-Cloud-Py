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


class ArrayInfoUpdate(object):
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
        "description": "str",
        "name": "str",
        "uri": "str",
        "access_credentials_name": "str",
    }

    attribute_map = {
        "description": "description",
        "name": "name",
        "uri": "uri",
        "access_credentials_name": "access_credentials_name",
    }

    def __init__(
        self, description=None, name=None, uri=None, access_credentials_name=None
    ):  # noqa: E501
        """ArrayInfoUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._name = None
        self._uri = None
        self._access_credentials_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if uri is not None:
            self.uri = uri
        if access_credentials_name is not None:
            self.access_credentials_name = access_credentials_name

    @property
    def description(self):
        """Gets the description of this ArrayInfoUpdate.  # noqa: E501

        description of array  # noqa: E501

        :return: The description of this ArrayInfoUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArrayInfoUpdate.

        description of array  # noqa: E501

        :param description: The description of this ArrayInfoUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ArrayInfoUpdate.  # noqa: E501

        description of array  # noqa: E501

        :return: The name of this ArrayInfoUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArrayInfoUpdate.

        description of array  # noqa: E501

        :param name: The name of this ArrayInfoUpdate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uri(self):
        """Gets the uri of this ArrayInfoUpdate.  # noqa: E501

        uri of array  # noqa: E501

        :return: The uri of this ArrayInfoUpdate.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ArrayInfoUpdate.

        uri of array  # noqa: E501

        :param uri: The uri of this ArrayInfoUpdate.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def access_credentials_name(self):
        """Gets the access_credentials_name of this ArrayInfoUpdate.  # noqa: E501

        the name of the access credentials to use. if unset, the default credentials will be used  # noqa: E501

        :return: The access_credentials_name of this ArrayInfoUpdate.  # noqa: E501
        :rtype: str
        """
        return self._access_credentials_name

    @access_credentials_name.setter
    def access_credentials_name(self, access_credentials_name):
        """Sets the access_credentials_name of this ArrayInfoUpdate.

        the name of the access credentials to use. if unset, the default credentials will be used  # noqa: E501

        :param access_credentials_name: The access_credentials_name of this ArrayInfoUpdate.  # noqa: E501
        :type: str
        """

        self._access_credentials_name = access_credentials_name

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
        if not isinstance(other, ArrayInfoUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
