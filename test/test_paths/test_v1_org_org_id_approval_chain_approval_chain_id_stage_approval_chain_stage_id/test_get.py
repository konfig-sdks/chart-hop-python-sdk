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
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id import get
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1OrgOrgIdApprovalChainApprovalChainIdStageApprovalChainStageId(ApiTestMixin, unittest.TestCase):
    """
    V1OrgOrgIdApprovalChainApprovalChainIdStageApprovalChainStageId unit test stubs
        Return all approval chain stages for an approval chain
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
