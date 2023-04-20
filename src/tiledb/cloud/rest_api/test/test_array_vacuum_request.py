# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import unittest

import tiledb.cloud.rest_api
from tiledb.cloud.rest_api.models.array_vacuum_request import (  # noqa: E501
    ArrayVacuumRequest,
)
from tiledb.cloud.rest_api.rest import ApiException


class TestArrayVacuumRequest(unittest.TestCase):
    """ArrayVacuumRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArrayVacuumRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.array_vacuum_request.ArrayVacuumRequest()  # noqa: E501
        if include_optional:
            return ArrayVacuumRequest(
                config=tiledb.cloud.rest_api.models.tile_db_config.TileDBConfig(
                    entries=[
                        tiledb.cloud.rest_api.models.tile_db_config_entries.TileDBConfig_entries(
                            key="0",
                            value="0",
                        )
                    ],
                )
            )
        else:
            return ArrayVacuumRequest()

    def testArrayVacuumRequest(self):
        """Test ArrayVacuumRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
