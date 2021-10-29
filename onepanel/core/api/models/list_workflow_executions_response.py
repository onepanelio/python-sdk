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


class ListWorkflowExecutionsResponse(object):
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
        'workflow_executions': 'list[WorkflowExecution]',
        'page': 'int',
        'pages': 'int',
        'total_count': 'int',
        'total_available_count': 'int'
    }

    attribute_map = {
        'count': 'count',
        'workflow_executions': 'workflowExecutions',
        'page': 'page',
        'pages': 'pages',
        'total_count': 'totalCount',
        'total_available_count': 'totalAvailableCount'
    }

    def __init__(self, count=None, workflow_executions=None, page=None, pages=None, total_count=None, total_available_count=None, local_vars_configuration=None):  # noqa: E501
        """ListWorkflowExecutionsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._workflow_executions = None
        self._page = None
        self._pages = None
        self._total_count = None
        self._total_available_count = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if workflow_executions is not None:
            self.workflow_executions = workflow_executions
        if page is not None:
            self.page = page
        if pages is not None:
            self.pages = pages
        if total_count is not None:
            self.total_count = total_count
        if total_available_count is not None:
            self.total_available_count = total_available_count

    @property
    def count(self):
        """Gets the count of this ListWorkflowExecutionsResponse.  # noqa: E501


        :return: The count of this ListWorkflowExecutionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkflowExecutionsResponse.


        :param count: The count of this ListWorkflowExecutionsResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def workflow_executions(self):
        """Gets the workflow_executions of this ListWorkflowExecutionsResponse.  # noqa: E501


        :return: The workflow_executions of this ListWorkflowExecutionsResponse.  # noqa: E501
        :rtype: list[WorkflowExecution]
        """
        return self._workflow_executions

    @workflow_executions.setter
    def workflow_executions(self, workflow_executions):
        """Sets the workflow_executions of this ListWorkflowExecutionsResponse.


        :param workflow_executions: The workflow_executions of this ListWorkflowExecutionsResponse.  # noqa: E501
        :type: list[WorkflowExecution]
        """

        self._workflow_executions = workflow_executions

    @property
    def page(self):
        """Gets the page of this ListWorkflowExecutionsResponse.  # noqa: E501


        :return: The page of this ListWorkflowExecutionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListWorkflowExecutionsResponse.


        :param page: The page of this ListWorkflowExecutionsResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def pages(self):
        """Gets the pages of this ListWorkflowExecutionsResponse.  # noqa: E501


        :return: The pages of this ListWorkflowExecutionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ListWorkflowExecutionsResponse.


        :param pages: The pages of this ListWorkflowExecutionsResponse.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def total_count(self):
        """Gets the total_count of this ListWorkflowExecutionsResponse.  # noqa: E501


        :return: The total_count of this ListWorkflowExecutionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListWorkflowExecutionsResponse.


        :param total_count: The total_count of this ListWorkflowExecutionsResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def total_available_count(self):
        """Gets the total_available_count of this ListWorkflowExecutionsResponse.  # noqa: E501


        :return: The total_available_count of this ListWorkflowExecutionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_available_count

    @total_available_count.setter
    def total_available_count(self, total_available_count):
        """Sets the total_available_count of this ListWorkflowExecutionsResponse.


        :param total_available_count: The total_available_count of this ListWorkflowExecutionsResponse.  # noqa: E501
        :type: int
        """

        self._total_available_count = total_available_count

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
        if not isinstance(other, ListWorkflowExecutionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListWorkflowExecutionsResponse):
            return True

        return self.to_dict() != other.to_dict()
