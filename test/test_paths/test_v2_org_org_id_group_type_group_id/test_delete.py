# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

import unittest
from unittest.mock import patch

import urllib3

import chart_hop_python_sdk
from chart_hop_python_sdk.paths.v2_org_org_id_group_type_group_id import delete
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2OrgOrgIdGroupTypeGroupId(ApiTestMixin, unittest.TestCase):
    """
    V2OrgOrgIdGroupTypeGroupId unit test stubs
        Delete a group
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202
    response_body = ''


if __name__ == '__main__':
    unittest.main()
