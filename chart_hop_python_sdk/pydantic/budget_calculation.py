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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.budget_calculation_job_budget_map import BudgetCalculationJobBudgetMap
from chart_hop_python_sdk.pydantic.pool_calculation import PoolCalculation

class BudgetCalculation(BaseModel):
    # the total budget amount
    allocated: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='allocated')

    # a list of budget pools that make up the total amount
    pools: typing.List[PoolCalculation] = Field(alias='pools')

    # the amount of the budget that has been used
    used: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='used')

    job_budget_map: typing.Optional[BudgetCalculationJobBudgetMap] = Field(None, alias='jobBudgetMap')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
