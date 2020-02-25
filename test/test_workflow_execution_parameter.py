# coding: utf-8

"""
    metric.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import core.api
from core.api.models.workflow_execution_parameter import WorkflowExecutionParameter  # noqa: E501
from core.api.rest import ApiException

class TestWorkflowExecutionParameter(unittest.TestCase):
    """WorkflowExecutionParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowExecutionParameter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = core.api.models.workflow_execution_parameter.WorkflowExecutionParameter()  # noqa: E501
        if include_optional :
            return WorkflowExecutionParameter(
                name = '0', 
                value = '0'
            )
        else :
            return WorkflowExecutionParameter(
        )

    def testWorkflowExecutionParameter(self):
        """Test WorkflowExecutionParameter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()