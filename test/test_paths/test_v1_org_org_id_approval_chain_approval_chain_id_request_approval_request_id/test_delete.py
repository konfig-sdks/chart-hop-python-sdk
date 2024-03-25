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
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id import delete
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1OrgOrgIdApprovalChainApprovalChainIdRequestApprovalRequestId(ApiTestMixin, unittest.TestCase):
    """
    V1OrgOrgIdApprovalChainApprovalChainIdRequestApprovalRequestId unit test stubs
        Delete an approval request
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202
    response_body = ''


if __name__ == '__main__':
    unittest.main()
