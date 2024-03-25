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
from chart_hop_python_sdk.paths.saml_org_org_id_xml_cert import post
from chart_hop_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSamlOrgOrgIdXmlCert(ApiTestMixin, unittest.TestCase):
    """
    SamlOrgOrgIdXmlCert unit test stubs
        Save per org Xml Cert from IDP
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 0
    response_body = ''


if __name__ == '__main__':
    unittest.main()
