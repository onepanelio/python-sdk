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
from onepanel.core.api.models.node_pool import NodePool  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestNodePool(unittest.TestCase):
    """NodePool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NodePool
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.node_pool.NodePool()  # noqa: E501
        if include_optional :
            return NodePool(
                label = '0', 
                options = [
                    onepanel.core.api.models.node_pool_option.NodePoolOption(
                        name = '0', 
                        value = '0', )
                    ]
            )
        else :
            return NodePool(
        )

    def testNodePool(self):
        """Test NodePool"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
