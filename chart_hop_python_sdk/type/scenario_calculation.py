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


class RequiredScenarioCalculation(TypedDict):
    # scenario id
    scenarioId: str

    # budget pool total allocation for scenario
    allocated: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalScenarioCalculation(TypedDict, total=False):
    # budget pool total use for scenario
    used: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class ScenarioCalculation(RequiredScenarioCalculation, OptionalScenarioCalculation):
    pass
