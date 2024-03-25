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
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id_job_job_id import patch
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2OrgOrgIdPositionPositionIdJobJobId(ApiTestMixin, unittest.TestCase):
    """
    V2OrgOrgIdPositionPositionIdJobJobId unit test stubs
        Update assign or remove date of a job for a position
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()