# coding: utf-8

"""
    Tiledb Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import unittest

import tiledb.cloud._common.api_v2
from tiledb.cloud._common.api_v2.models.float_scale_config import (  # noqa: E501
    FloatScaleConfig,
)
from tiledb.cloud._common.api_v2.rest import ApiException


class TestFloatScaleConfig(unittest.TestCase):
    """FloatScaleConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FloatScaleConfig
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud._common.api_v2.models.float_scale_config.FloatScaleConfig()  # noqa: E501
        if include_optional:
            return FloatScaleConfig(scale=56, offset=56, byte_width=56)
        else:
            return FloatScaleConfig()

    def testFloatScaleConfig(self):
        """Test FloatScaleConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
