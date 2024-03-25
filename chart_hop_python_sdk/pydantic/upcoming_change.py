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


class UpcomingChange(BaseModel):
    date: date = Field(alias='date')

    id: typing.Optional[str] = Field(None, alias='id')

    type: typing.Optional[Literal["HIRE", "DEPART", "MOVE", "UPCOMING", "CREATE", "UPDATE", "DATA", "DELETE", "RELATE", "BACKFILL"]] = Field(None, alias='type')

    announce_date: typing.Optional[date] = Field(None, alias='announceDate')

    person_id: typing.Optional[str] = Field(None, alias='personId')

    other_person_id: typing.Optional[str] = Field(None, alias='otherPersonId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
