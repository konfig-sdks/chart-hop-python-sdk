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


class UpdateTimeOffEntity(BaseModel):
    # external identifier, if time off synced from external system
    external_id: typing.Optional[str] = Field(None, alias='externalId')

    # start date of time off, inclusive
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    # end date of time off, inclusive
    end_date: typing.Optional[date] = Field(None, alias='endDate')

    # number of days used
    days: typing.Optional[typing.Union[int, float]] = Field(None, alias='days')

    # number of hours used
    hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='hours')

    # type of time off
    type_description: typing.Optional[str] = Field(None, alias='typeDescription')

    # notes on the time off
    note: typing.Optional[str] = Field(None, alias='note')

    # approval status of the time off
    approval: typing.Optional[Literal["APPROVED", "PENDING", "CANCELLED", "REJECTED", "SUPERSEDED"]] = Field(None, alias='approval')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
