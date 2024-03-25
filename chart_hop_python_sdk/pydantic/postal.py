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

from chart_hop_python_sdk.pydantic.geopoint import Geopoint

class Postal(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # postal code
    postal: typing.Optional[str] = Field(None, alias='postal')

    # city name
    city: typing.Optional[str] = Field(None, alias='city')

    # state code
    state: typing.Optional[str] = Field(None, alias='state')

    # country code
    country: typing.Optional[str] = Field(None, alias='country')

    geo: typing.Optional[Geopoint] = Field(None, alias='geo')

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
