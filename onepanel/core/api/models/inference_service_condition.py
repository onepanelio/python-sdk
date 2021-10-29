# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class InferenceServiceCondition(object):
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
        'last_transition_time': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'last_transition_time': 'lastTransitionTime',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, last_transition_time=None, status=None, type=None, local_vars_configuration=None):  # noqa: E501
        """InferenceServiceCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_transition_time = None
        self._status = None
        self._type = None
        self.discriminator = None

        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this InferenceServiceCondition.  # noqa: E501


        :return: The last_transition_time of this InferenceServiceCondition.  # noqa: E501
        :rtype: str
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this InferenceServiceCondition.


        :param last_transition_time: The last_transition_time of this InferenceServiceCondition.  # noqa: E501
        :type: str
        """

        self._last_transition_time = last_transition_time

    @property
    def status(self):
        """Gets the status of this InferenceServiceCondition.  # noqa: E501


        :return: The status of this InferenceServiceCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InferenceServiceCondition.


        :param status: The status of this InferenceServiceCondition.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this InferenceServiceCondition.  # noqa: E501


        :return: The type of this InferenceServiceCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InferenceServiceCondition.


        :param type: The type of this InferenceServiceCondition.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, InferenceServiceCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InferenceServiceCondition):
            return True

        return self.to_dict() != other.to_dict()
