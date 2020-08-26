# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: v0.12.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class ListWorkflowTemplateVersionsResponse(object):
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
        'count': 'int',
        'workflow_templates': 'list[WorkflowTemplate]'
    }

    attribute_map = {
        'count': 'count',
        'workflow_templates': 'workflowTemplates'
    }

    def __init__(self, count=None, workflow_templates=None, local_vars_configuration=None):  # noqa: E501
        """ListWorkflowTemplateVersionsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._workflow_templates = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if workflow_templates is not None:
            self.workflow_templates = workflow_templates

    @property
    def count(self):
        """Gets the count of this ListWorkflowTemplateVersionsResponse.  # noqa: E501


        :return: The count of this ListWorkflowTemplateVersionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkflowTemplateVersionsResponse.


        :param count: The count of this ListWorkflowTemplateVersionsResponse.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def workflow_templates(self):
        """Gets the workflow_templates of this ListWorkflowTemplateVersionsResponse.  # noqa: E501


        :return: The workflow_templates of this ListWorkflowTemplateVersionsResponse.  # noqa: E501
        :rtype: list[WorkflowTemplate]
        """
        return self._workflow_templates

    @workflow_templates.setter
    def workflow_templates(self, workflow_templates):
        """Sets the workflow_templates of this ListWorkflowTemplateVersionsResponse.


        :param workflow_templates: The workflow_templates of this ListWorkflowTemplateVersionsResponse.  # noqa: E501
        :type workflow_templates: list[WorkflowTemplate]
        """

        self._workflow_templates = workflow_templates

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
        if not isinstance(other, ListWorkflowTemplateVersionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListWorkflowTemplateVersionsResponse):
            return True

        return self.to_dict() != other.to_dict()
