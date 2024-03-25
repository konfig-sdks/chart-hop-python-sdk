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


class ProcessEventUpdatePayload(BaseModel):
    key: typing.Optional[str] = Field(None, alias='key')

    value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='value')

    currency: typing.Optional[str] = Field(None, alias='currency')

    contact_format: typing.Optional[Literal["PHONE", "EMAIL", "ID"]] = Field(None, alias='contactFormat')

    error_message: typing.Optional[str] = Field(None, alias='errorMessage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
