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
from onepanel.core.api.models.node_pool_option import NodePoolOption  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestNodePoolOption(unittest.TestCase):
    """NodePoolOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NodePoolOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.node_pool_option.NodePoolOption()  # noqa: E501
        if include_optional :
            return NodePoolOption(
                name = '0', 
                value = '0'
            )
        else :
            return NodePoolOption(
        )

    def testNodePoolOption(self):
        """Test NodePoolOption"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
