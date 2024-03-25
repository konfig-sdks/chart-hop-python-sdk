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

from chart_hop_python_sdk.type.budget_calculation_job_budget_map import BudgetCalculationJobBudgetMap
from chart_hop_python_sdk.type.pool_calculation import PoolCalculation

class RequiredBudgetCalculation(TypedDict):
    # the total budget amount
    allocated: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # a list of budget pools that make up the total amount
    pools: typing.List[PoolCalculation]

class OptionalBudgetCalculation(TypedDict, total=False):
    # the amount of the budget that has been used
    used: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    jobBudgetMap: BudgetCalculationJobBudgetMap

class BudgetCalculation(RequiredBudgetCalculation, OptionalBudgetCalculation):
    pass
