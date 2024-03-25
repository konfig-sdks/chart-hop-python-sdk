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

class RequiredPostal(TypedDict):
    # globally unique id
    id: str

class OptionalPostal(TypedDict, total=False):
    # postal code
    postal: str

    # city name
    city: str

    # state code
    state: str

    # country code
    country: str

    geo: Geopoint

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class Postal(RequiredPostal, OptionalPostal):
    pass
