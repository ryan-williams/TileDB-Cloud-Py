# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.6.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AWSAccessCredentials(object):
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
        'secret_access_key': 'str',
        'access_key_id': 'str',
        'service_role_arn': 'str',
        'name': 'str',
        'default': 'bool',
        'buckets': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'secret_access_key': 'secret_access_key',
        'access_key_id': 'access_key_id',
        'service_role_arn': 'service_role_arn',
        'name': 'name',
        'default': 'default',
        'buckets': 'buckets',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, secret_access_key=None, access_key_id=None, service_role_arn=None, name=None, default=None, buckets=None, created_at=None, updated_at=None):  # noqa: E501
        """AWSAccessCredentials - a model defined in OpenAPI"""  # noqa: E501

        self._secret_access_key = None
        self._access_key_id = None
        self._service_role_arn = None
        self._name = None
        self._default = None
        self._buckets = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if service_role_arn is not None:
            self.service_role_arn = service_role_arn
        if name is not None:
            self.name = name
        if default is not None:
            self.default = default
        if buckets is not None:
            self.buckets = buckets
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this AWSAccessCredentials.  # noqa: E501

        aws secret access key, never returned in get requests  # noqa: E501

        :return: The secret_access_key of this AWSAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this AWSAccessCredentials.

        aws secret access key, never returned in get requests  # noqa: E501

        :param secret_access_key: The secret_access_key of this AWSAccessCredentials.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def access_key_id(self):
        """Gets the access_key_id of this AWSAccessCredentials.  # noqa: E501

        aws access key  # noqa: E501

        :return: The access_key_id of this AWSAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this AWSAccessCredentials.

        aws access key  # noqa: E501

        :param access_key_id: The access_key_id of this AWSAccessCredentials.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def service_role_arn(self):
        """Gets the service_role_arn of this AWSAccessCredentials.  # noqa: E501

        aws service role to use for access  # noqa: E501

        :return: The service_role_arn of this AWSAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._service_role_arn

    @service_role_arn.setter
    def service_role_arn(self, service_role_arn):
        """Sets the service_role_arn of this AWSAccessCredentials.

        aws service role to use for access  # noqa: E501

        :param service_role_arn: The service_role_arn of this AWSAccessCredentials.  # noqa: E501
        :type: str
        """

        self._service_role_arn = service_role_arn

    @property
    def name(self):
        """Gets the name of this AWSAccessCredentials.  # noqa: E501

        human readable name  # noqa: E501

        :return: The name of this AWSAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AWSAccessCredentials.

        human readable name  # noqa: E501

        :param name: The name of this AWSAccessCredentials.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def default(self):
        """Gets the default of this AWSAccessCredentials.  # noqa: E501

        true if this is the default credential to be used within this namespace  # noqa: E501

        :return: The default of this AWSAccessCredentials.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AWSAccessCredentials.

        true if this is the default credential to be used within this namespace  # noqa: E501

        :param default: The default of this AWSAccessCredentials.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def buckets(self):
        """Gets the buckets of this AWSAccessCredentials.  # noqa: E501

        a whitelist of one or more buckets this key should access  # noqa: E501

        :return: The buckets of this AWSAccessCredentials.  # noqa: E501
        :rtype: list[str]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this AWSAccessCredentials.

        a whitelist of one or more buckets this key should access  # noqa: E501

        :param buckets: The buckets of this AWSAccessCredentials.  # noqa: E501
        :type: list[str]
        """

        self._buckets = buckets

    @property
    def created_at(self):
        """Gets the created_at of this AWSAccessCredentials.  # noqa: E501

        Time when udf dependencies was created (rfc3339)  # noqa: E501

        :return: The created_at of this AWSAccessCredentials.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AWSAccessCredentials.

        Time when udf dependencies was created (rfc3339)  # noqa: E501

        :param created_at: The created_at of this AWSAccessCredentials.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AWSAccessCredentials.  # noqa: E501

        Time when udf dependencies was last updated (rfc3339)  # noqa: E501

        :return: The updated_at of this AWSAccessCredentials.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AWSAccessCredentials.

        Time when udf dependencies was last updated (rfc3339)  # noqa: E501

        :param updated_at: The updated_at of this AWSAccessCredentials.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AWSAccessCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
