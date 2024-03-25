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


class EnumValue(BaseModel):
    # enum value name
    name: str = Field(alias='name')

    # enum value label
    label: str = Field(alias='label')

    # color of property
    color: typing.Optional[str] = Field(None, alias='color')

    # computed expression, for ENUM_EXPR type
    expr: typing.Optional[str] = Field(None, alias='expr')

    # numeric value, for ENUM_SCALE type
    num: typing.Optional[typing.Union[int, float]] = Field(None, alias='num')

    # unique identifier for enum
    id: typing.Optional[str] = Field(None, alias='id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
