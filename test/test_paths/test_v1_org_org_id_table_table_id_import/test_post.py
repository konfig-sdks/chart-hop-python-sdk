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
from chart_hop_python_sdk.paths.v1_org_org_id_table_table_id_import import post
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1OrgOrgIdTableTableIdImport(ApiTestMixin, unittest.TestCase):
    """
    V1OrgOrgIdTableTableIdImport unit test stubs
        Import data from CSV file
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202




if __name__ == '__main__':
    unittest.main()
