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

from chart_hop_python_sdk.pydantic.money import Money

class PayInterval(BaseModel):
    # Interval (annual or hourly)
    interval: Literal["YEARLY", "HOURLY"] = Field(alias='interval')

    pay: Money = Field(alias='pay')

    # working hours per week if interval=hourly
    hours_per_week: typing.Optional[int] = Field(None, alias='hoursPerWeek')

    # working weeks per year if interval=hourly
    weeks_per_year: typing.Optional[int] = Field(None, alias='weeksPerYear')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
