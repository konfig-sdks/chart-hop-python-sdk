# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

import unittest

import os
from pprint import pprint
from chart_hop_python_sdk import ChartHop

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        charthop = ChartHop(
        )
        self.assertIsNotNone(charthop)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
