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


class UpdateLegalDoc(BaseModel):
    # human-readable full name of form
    name: typing.Optional[str] = Field(None, alias='name')

    # legal doc content
    content: typing.Optional[str] = Field(None, alias='content')

    # content by date
    date: typing.Optional[date] = Field(None, alias='date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
