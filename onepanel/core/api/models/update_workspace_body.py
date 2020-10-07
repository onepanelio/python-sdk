# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.13.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class UpdateWorkspaceBody(object):
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
        'parameters': 'list[Parameter]',
        'labels': 'list[KeyValue]'
    }

    attribute_map = {
        'parameters': 'parameters',
        'labels': 'labels'
    }

    def __init__(self, parameters=None, labels=None, local_vars_configuration=None):  # noqa: E501
        """UpdateWorkspaceBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parameters = None
        self._labels = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if labels is not None:
            self.labels = labels

    @property
    def parameters(self):
        """Gets the parameters of this UpdateWorkspaceBody.  # noqa: E501


        :return: The parameters of this UpdateWorkspaceBody.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpdateWorkspaceBody.


        :param parameters: The parameters of this UpdateWorkspaceBody.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def labels(self):
        """Gets the labels of this UpdateWorkspaceBody.  # noqa: E501


        :return: The labels of this UpdateWorkspaceBody.  # noqa: E501
        :rtype: list[KeyValue]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this UpdateWorkspaceBody.


        :param labels: The labels of this UpdateWorkspaceBody.  # noqa: E501
        :type: list[KeyValue]
        """

        self._labels = labels

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
        if not isinstance(other, UpdateWorkspaceBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateWorkspaceBody):
            return True

        return self.to_dict() != other.to_dict()
