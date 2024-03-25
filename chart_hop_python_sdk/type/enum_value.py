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


class RequiredEnumValue(TypedDict):
    # enum value name
    name: str

    # enum value label
    label: str

class OptionalEnumValue(TypedDict, total=False):
    # color of property
    color: str

    # computed expression, for ENUM_EXPR type
    expr: str

    # numeric value, for ENUM_SCALE type
    num: typing.Union[int, float]

    # unique identifier for enum
    id: str

class EnumValue(RequiredEnumValue, OptionalEnumValue):
    pass
