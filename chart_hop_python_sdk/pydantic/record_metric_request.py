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


class RecordMetricRequest(BaseModel):
    # the name of the metric, for example kpi.revenue.arr
    metric: str = Field(alias='metric')

    # the numeric value of the metric
    value: typing.Union[int, float] = Field(alias='value')

    # the date that the metric applies to (if blank, will default to today)
    date: typing.Optional[date] = Field(None, alias='date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
