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


class UpdateMultiplier(BaseModel):
    # human-readable name of multiplier
    label: typing.Optional[str] = Field(None, alias='label')

    code: typing.Optional[str] = Field(None, alias='code')

    # amount to multiply the initial value by
    value: typing.Optional[typing.Union[int, float]] = Field(None, alias='value')

    # calculated expression to match against the job
    expr: typing.Optional[str] = Field(None, alias='expr')

    # tag to group multipliers together by
    category: typing.Optional[str] = Field(None, alias='category')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
