# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from chart_hop_python_sdk.type.geopoint import Geopoint

class RequiredAddress(TypedDict):
    # country (two-digit ISO code)
    country: str

class OptionalAddress(TypedDict, total=False):
    # street address, line 1
    street1: str

    # street address, line 2
    street2: str

    # street address, line 3
    street3: str

    # city
    city: str

    # state
    state: str

    # postal code
    postal: str

    geo: Geopoint

    approxGeo: Geopoint

class Address(RequiredAddress, OptionalAddress):
    pass
