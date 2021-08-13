# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.inference_service_transformer import InferenceServiceTransformer  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestInferenceServiceTransformer(unittest.TestCase):
    """InferenceServiceTransformer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InferenceServiceTransformer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.inference_service_transformer.InferenceServiceTransformer()  # noqa: E501
        if include_optional :
            return InferenceServiceTransformer(
                containers = [
                    onepanel.core.api.models.container.Container(
                        image = '0', 
                        name = '0', 
                        env = [
                            onepanel.core.api.models.env.Env(
                                name = '0', 
                                value = '0', )
                            ], )
                    ], 
                min_cpu = '0', 
                min_memory = '0', 
                max_cpu = '0', 
                max_memory = '0'
            )
        else :
            return InferenceServiceTransformer(
        )

    def testInferenceServiceTransformer(self):
        """Test InferenceServiceTransformer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()