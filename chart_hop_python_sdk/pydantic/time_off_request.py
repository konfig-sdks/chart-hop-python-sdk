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


class TimeOffRequest(BaseModel):
    start_date: date = Field(alias='startDate')

    end_date: date = Field(alias='endDate')

    person_id: typing.Optional[str] = Field(None, alias='personId')

    type_description: typing.Optional[str] = Field(None, alias='typeDescription')

    note: typing.Optional[str] = Field(None, alias='note')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
