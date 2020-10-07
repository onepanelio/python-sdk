# coding: utf-8

"""
    workflow.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.delete_secret_key_response import DeleteSecretKeyResponse  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestDeleteSecretKeyResponse(unittest.TestCase):
    """DeleteSecretKeyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeleteSecretKeyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.delete_secret_key_response.DeleteSecretKeyResponse()  # noqa: E501
        if include_optional :
            return DeleteSecretKeyResponse(
                deleted = True
            )
        else :
            return DeleteSecretKeyResponse(
        )

    def testDeleteSecretKeyResponse(self):
        """Test DeleteSecretKeyResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
