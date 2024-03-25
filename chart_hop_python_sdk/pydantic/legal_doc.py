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


class LegalDoc(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # human-readable full name of form
    name: str = Field(alias='name')

    # content by date
    date: date = Field(alias='date')

    # legal doc content
    content: typing.Optional[str] = Field(None, alias='content')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )