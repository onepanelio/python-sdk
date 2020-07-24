# coding: utf-8

"""
    Onepanel Core

    Onepanel Core project API  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.update_secret_key_value_response import UpdateSecretKeyValueResponse  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestUpdateSecretKeyValueResponse(unittest.TestCase):
    """UpdateSecretKeyValueResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateSecretKeyValueResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.update_secret_key_value_response.UpdateSecretKeyValueResponse()  # noqa: E501
        if include_optional :
            return UpdateSecretKeyValueResponse(
                updated = True
            )
        else :
            return UpdateSecretKeyValueResponse(
        )

    def testUpdateSecretKeyValueResponse(self):
        """Test UpdateSecretKeyValueResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
