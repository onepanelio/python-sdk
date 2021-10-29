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
from onepanel.core.api.models.inference_service_predictor import InferenceServicePredictor  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestInferenceServicePredictor(unittest.TestCase):
    """InferenceServicePredictor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InferenceServicePredictor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.inference_service_predictor.InferenceServicePredictor()  # noqa: E501
        if include_optional :
            return InferenceServicePredictor(
                name = '0', 
                runtime_version = '0', 
                storage_uri = '0', 
                node_selector = '0', 
                min_cpu = '0', 
                min_memory = '0', 
                max_cpu = '0', 
                max_memory = '0'
            )
        else :
            return InferenceServicePredictor(
        )

    def testInferenceServicePredictor(self):
        """Test InferenceServicePredictor"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
