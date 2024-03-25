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


class LabelOverride(BaseModel):
    # The unique identifier to use to locate the key to override. For entities and enum values, this will be an id. For numbers, this will be the normalized numeric representation. For others, this will be the string
    id: str = Field(alias='id')

    # If set, overrides this label
    label: typing.Optional[str] = Field(None, alias='label')

    # If set, overrides the default color
    color: typing.Optional[str] = Field(None, alias='color')

    # If set, overrides the sorting order
    sort: typing.Optional[int] = Field(None, alias='sort')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
