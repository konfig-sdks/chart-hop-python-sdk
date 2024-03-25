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
from chart_hop_python_sdk.paths.v1_user_assign import patch
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1UserAssign(ApiTestMixin, unittest.TestCase):
    """
    V1UserAssign unit test stubs
        Assign or remove multiple users a role within an org
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()