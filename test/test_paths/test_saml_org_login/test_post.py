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
from chart_hop_python_sdk.paths.saml_org_login import post
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSamlOrgLogin(ApiTestMixin, unittest.TestCase):
    """
    SamlOrgLogin unit test stubs
        Return an redirect to the designated Idp, given an identity provider
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 0
    response_body = ''


if __name__ == '__main__':
    unittest.main()
