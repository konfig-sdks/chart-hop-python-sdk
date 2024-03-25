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

from chart_hop_python_sdk.type.scenario_calculation import ScenarioCalculation

class RequiredPoolCalculation(TypedDict):
    # budget pool id
    budgetPoolId: str

    # budget pool label
    label: str

    # budget pool total amount
    allocated: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # a list of reviewer/scenario specific calculations that create the total
    scenarios: typing.List[ScenarioCalculation]

class OptionalPoolCalculation(TypedDict, total=False):
    # the amount of the budget pool that has been used
    used: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class PoolCalculation(RequiredPoolCalculation, OptionalPoolCalculation):
    pass
