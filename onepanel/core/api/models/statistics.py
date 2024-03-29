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


class Statistics(object):
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
        'workflow_status': 'str',
        'workflow_template_id': 'str'
    }

    attribute_map = {
        'workflow_status': 'workflowStatus',
        'workflow_template_id': 'workflowTemplateId'
    }

    def __init__(self, workflow_status=None, workflow_template_id=None, local_vars_configuration=None):  # noqa: E501
        """Statistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._workflow_status = None
        self._workflow_template_id = None
        self.discriminator = None

        if workflow_status is not None:
            self.workflow_status = workflow_status
        if workflow_template_id is not None:
            self.workflow_template_id = workflow_template_id

    @property
    def workflow_status(self):
        """Gets the workflow_status of this Statistics.  # noqa: E501


        :return: The workflow_status of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """Sets the workflow_status of this Statistics.


        :param workflow_status: The workflow_status of this Statistics.  # noqa: E501
        :type: str
        """

        self._workflow_status = workflow_status

    @property
    def workflow_template_id(self):
        """Gets the workflow_template_id of this Statistics.  # noqa: E501


        :return: The workflow_template_id of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._workflow_template_id

    @workflow_template_id.setter
    def workflow_template_id(self, workflow_template_id):
        """Sets the workflow_template_id of this Statistics.


        :param workflow_template_id: The workflow_template_id of this Statistics.  # noqa: E501
        :type: str
        """

        self._workflow_template_id = workflow_template_id

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
        if not isinstance(other, Statistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Statistics):
            return True

        return self.to_dict() != other.to_dict()
