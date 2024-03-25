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


class PlanTier(BaseModel):
    # PEPM rate
    unit_amount: typing.Union[int, float] = Field(alias='unitAmount')

    # headcount up to this level is charged at the below rate
    up_to: typing.Optional[int] = Field(None, alias='upTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
