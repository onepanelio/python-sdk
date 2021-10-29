# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.list_workflow_template_versions_response import ListWorkflowTemplateVersionsResponse  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestListWorkflowTemplateVersionsResponse(unittest.TestCase):
    """ListWorkflowTemplateVersionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListWorkflowTemplateVersionsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.list_workflow_template_versions_response.ListWorkflowTemplateVersionsResponse()  # noqa: E501
        if include_optional :
            return ListWorkflowTemplateVersionsResponse(
                count = 56, 
                workflow_templates = [
                    onepanel.core.api.models.workflow_template.WorkflowTemplate(
                        created_at = '0', 
                        modified_at = '0', 
                        uid = '0', 
                        name = '0', 
                        version = '0', 
                        versions = '0', 
                        manifest = '0', 
                        is_latest = True, 
                        is_archived = True, 
                        labels = [
                            onepanel.core.api.models.key_value.KeyValue(
                                key = '0', 
                                value = '0', )
                            ], 
                        stats = onepanel.core.api.models.workflow_execution_statistic_report.WorkflowExecutionStatisticReport(
                            total = 56, 
                            last_executed = '0', 
                            running = 56, 
                            completed = 56, 
                            failed = 56, 
                            terminated = 56, ), 
                        cron_stats = onepanel.core.api.models.cron_workflow_statistics_report.CronWorkflowStatisticsReport(
                            total = 56, ), 
                        parameters = [
                            onepanel.core.api.models.parameter.Parameter(
                                name = '0', 
                                value = '0', 
                                type = '0', 
                                display_name = '0', 
                                hint = '0', 
                                required = True, 
                                visibility = '0', 
                                options = [
                                    onepanel.core.api.models.parameter_option.ParameterOption(
                                        name = '0', 
                                        value = '0', )
                                    ], )
                            ], 
                        description = '0', )
                    ]
            )
        else :
            return ListWorkflowTemplateVersionsResponse(
        )

    def testListWorkflowTemplateVersionsResponse(self):
        """Test ListWorkflowTemplateVersionsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
