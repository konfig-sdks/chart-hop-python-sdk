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


class RequiredAdjustScenarioDateRequest(TypedDict):
    pass

class OptionalAdjustScenarioDateRequest(TypedDict, total=False):
    # date to use as new start date
    date: date

    # number of days to adjust forward
    days: int

class AdjustScenarioDateRequest(RequiredAdjustScenarioDateRequest, OptionalAdjustScenarioDateRequest):
    pass
