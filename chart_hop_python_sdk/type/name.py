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


class RequiredName(TypedDict):
    # last name
    last: str

class OptionalName(TypedDict, total=False):
    # first name
    first: str

    # middle name
    middle: str

    # preferred first name
    pref: str

    # preferred last name
    prefLast: str

class Name(RequiredName, OptionalName):
    pass
