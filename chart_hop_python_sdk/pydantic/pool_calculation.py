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

from chart_hop_python_sdk.pydantic.scenario_calculation import ScenarioCalculation

class PoolCalculation(BaseModel):
    # budget pool id
    budget_pool_id: str = Field(alias='budgetPoolId')

    # budget pool label
    label: str = Field(alias='label')

    # budget pool total amount
    allocated: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='allocated')

    # a list of reviewer/scenario specific calculations that create the total
    scenarios: typing.List[ScenarioCalculation] = Field(alias='scenarios')

    # the amount of the budget pool that has been used
    used: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='used')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
