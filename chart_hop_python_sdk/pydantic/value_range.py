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


class ValueRange(BaseModel):
    # the maximum value in the range (type = BigDecimal)
    max: typing.Optional[typing.Union[int, float]] = Field(None, alias='max')

    # the minimum value in the range (type = BigDecimal)
    min: typing.Optional[typing.Union[int, float]] = Field(None, alias='min')

    # the target value for the range (type = BigDecimal)
    target: typing.Optional[typing.Union[int, float]] = Field(None, alias='target')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
