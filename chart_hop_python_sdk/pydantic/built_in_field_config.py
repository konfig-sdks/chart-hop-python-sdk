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


class BuiltInFieldConfig(BaseModel):
    # reserved codename for the native field
    name: str = Field(alias='name')

    # hidden state of the native field (specific to org)
    hidden: bool = Field(alias='hidden')

    # decimal places to round native Money fields
    places: typing.Optional[int] = Field(None, alias='places')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
