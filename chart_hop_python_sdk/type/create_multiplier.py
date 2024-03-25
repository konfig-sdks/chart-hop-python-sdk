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


class RequiredCreateMultiplier(TypedDict):
    # human-readable name of multiplier
    label: str

    # amount to multiply the initial value by
    value: typing.Union[int, float]

    # calculated expression to match against the job
    expr: str

class OptionalCreateMultiplier(TypedDict, total=False):
    code: str

    # tag to group multipliers together by
    category: str

class CreateMultiplier(RequiredCreateMultiplier, OptionalCreateMultiplier):
    pass
