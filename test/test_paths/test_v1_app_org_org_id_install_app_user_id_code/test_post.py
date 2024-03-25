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
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id_code import post
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1AppOrgOrgIdInstallAppUserIdCode(ApiTestMixin, unittest.TestCase):
    """
    V1AppOrgOrgIdInstallAppUserIdCode unit test stubs
        Retrieve an Oauth2 authorization code for this app, which can be exchanged for an access token
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204




if __name__ == '__main__':
    unittest.main()
