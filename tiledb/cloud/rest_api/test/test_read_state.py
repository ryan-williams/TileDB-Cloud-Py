# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tiledb.cloud.rest_api
from tiledb.cloud.rest_api.models.read_state import ReadState  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestReadState(unittest.TestCase):
    """ReadState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReadState
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.read_state.ReadState()  # noqa: E501
        if include_optional:
            return ReadState(
                initialized=True,
                overflowed=True,
                unsplittable=True,
                subarray_partitioner=tiledb.cloud.rest_api.models.subarray_partitioner.SubarrayPartitioner(
                    subarray=tiledb.cloud.rest_api.models.subarray.Subarray(
                        layout="row-major",
                        ranges=[
                            tiledb.cloud.rest_api.models.subarray_ranges.SubarrayRanges(
                                type="INT32",
                                has_default_range=True,
                                buffer=[56],
                            )
                        ],
                    ),
                    budget=[
                        tiledb.cloud.rest_api.models.attribute_buffer_size.AttributeBufferSize(
                            attribute="0",
                            offset_bytes=56,
                            data_bytes=56,
                        )
                    ],
                    current=tiledb.cloud.rest_api.models.subarray_partitioner_current.SubarrayPartitioner_current(
                        start=56,
                        end=56,
                        split_multi_range=True,
                    ),
                    state=tiledb.cloud.rest_api.models.subarray_partitioner_state.SubarrayPartitioner_state(
                        start=56,
                        end=56,
                        single_range=[tiledb.cloud.rest_api.models.subarray.Subarray()],
                        multi_range=[tiledb.cloud.rest_api.models.subarray.Subarray()],
                    ),
                    memory_budget=56,
                    memory_budget_var=56,
                ),
            )
        else:
            return ReadState()

    def testReadState(self):
        """Test ReadState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
