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

from chart_hop_python_sdk.pydantic.money_range import MoneyRange
from chart_hop_python_sdk.pydantic.value_range import ValueRange

class BasisCondition(BaseModel):
    condition_expr: str = Field(alias='conditionExpr')

    amount_range: typing.Optional[MoneyRange] = Field(None, alias='amountRange')

    value_range: typing.Optional[ValueRange] = Field(None, alias='valueRange')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
