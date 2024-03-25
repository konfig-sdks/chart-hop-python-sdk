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

from chart_hop_python_sdk.type.change_data import ChangeData
from chart_hop_python_sdk.type.guideline_calculation import GuidelineCalculation

class RequiredInCycleChange(TypedDict):
    change: ChangeData

    guidelines: typing.List[GuidelineCalculation]

class OptionalInCycleChange(TypedDict, total=False):
    pass

class InCycleChange(RequiredInCycleChange, OptionalInCycleChange):
    pass
