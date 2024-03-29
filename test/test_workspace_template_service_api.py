# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.workspace_template_service_api import WorkspaceTemplateServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestWorkspaceTemplateServiceApi(unittest.TestCase):
    """WorkspaceTemplateServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.workspace_template_service_api.WorkspaceTemplateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_workspace_template(self):
        """Test case for archive_workspace_template

        Archives a WorkspaceTemplate  # noqa: E501
        """
        pass

    def test_create_workspace_template(self):
        """Test case for create_workspace_template

        Creates a WorkspaceTemplate  # noqa: E501
        """
        pass

    def test_generate_workspace_template_workflow_template(self):
        """Test case for generate_workspace_template_workflow_template

        Get the generated WorkflowTemplate for a WorkspaceTemplate  # noqa: E501
        """
        pass

    def test_get_workspace_template(self):
        """Test case for get_workspace_template

        Get a WorkspaceTemplate  # noqa: E501
        """
        pass

    def test_list_workspace_template_versions(self):
        """Test case for list_workspace_template_versions

        """
        pass

    def test_list_workspace_templates(self):
        """Test case for list_workspace_templates

        """
        pass

    def test_list_workspace_templates_field(self):
        """Test case for list_workspace_templates_field

        """
        pass

    def test_update_workspace_template(self):
        """Test case for update_workspace_template

        Updates a WorkspaceTemplate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
