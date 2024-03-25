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
from chart_hop_python_sdk.paths.oauth_sso_idp_login import get
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOauthSsoIdpLogin(ApiTestMixin, unittest.TestCase):
    """
    OauthSsoIdpLogin unit test stubs
        Login via the auth endpoint
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
