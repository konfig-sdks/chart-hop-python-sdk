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
from chart_hop_python_sdk.paths.oauth_sso_idp_access_token import get
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOauthSsoIdpAccessToken(ApiTestMixin, unittest.TestCase):
    """
    OauthSsoIdpAccessToken unit test stubs
        Exchange a one-time use Auth Code for the IDP access token response
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
