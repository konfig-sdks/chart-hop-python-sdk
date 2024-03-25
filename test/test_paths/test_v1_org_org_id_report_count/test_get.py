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
from chart_hop_python_sdk.paths.v1_org_org_id_report_count import get
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1OrgOrgIdReportCount(ApiTestMixin, unittest.TestCase):
    """
    V1OrgOrgIdReportCount unit test stubs
        Return count of reports in an organization
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()