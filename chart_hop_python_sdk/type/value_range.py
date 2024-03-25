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


class RequiredValueRange(TypedDict):
    pass

class OptionalValueRange(TypedDict, total=False):
    # the maximum value in the range (type = BigDecimal)
    max: typing.Union[int, float]

    # the minimum value in the range (type = BigDecimal)
    min: typing.Union[int, float]

    # the target value for the range (type = BigDecimal)
    target: typing.Union[int, float]

class ValueRange(RequiredValueRange, OptionalValueRange):
    pass
