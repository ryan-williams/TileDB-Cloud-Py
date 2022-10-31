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
from tiledb.cloud._common.api_v2.models.group_contents_changes_request import (  # noqa: E501
    GroupContentsChangesRequest,
)
from tiledb.cloud._common.api_v2.rest import ApiException


class TestGroupContentsChangesRequest(unittest.TestCase):
    """GroupContentsChangesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupContentsChangesRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud._common.api_v2.models.group_contents_changes_request.GroupContentsChangesRequest()  # noqa: E501
        if include_optional:
            return GroupContentsChangesRequest(
                config=tiledb.cloud._common.api_v2.models.tile_db_config.TileDBConfig(
                    entries=[
                        tiledb.cloud._common.api_v2.models.tile_db_config_entries.TileDBConfig_entries(
                            key="0",
                            value="0",
                        )
                    ],
                ),
                group_changes=tiledb.cloud._common.api_v2.models.group_contents_changes_request_group_changes.GroupContentsChangesRequest_group_changes(
                    members_to_remove=["0"],
                    members_to_add=[
                        tiledb.cloud._common.api_v2.models.group_member.GroupMember(
                            name="0",
                            uri="0",
                            type="GROUP",
                        )
                    ],
                ),
            )
        else:
            return GroupContentsChangesRequest()

    def testGroupContentsChangesRequest(self):
        """Test GroupContentsChangesRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
