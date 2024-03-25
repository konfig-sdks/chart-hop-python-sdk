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

from chart_hop_python_sdk.type.enum_value import EnumValue

class RequiredCreateJobLevel(TypedDict):
    # human-readable name of job level
    label: str

class OptionalCreateJobLevel(TypedDict, total=False):
    # job level code
    code: str

    benchmarkType: EnumValue

    benchmarkLevel: EnumValue

class CreateJobLevel(RequiredCreateJobLevel, OptionalCreateJobLevel):
    pass
