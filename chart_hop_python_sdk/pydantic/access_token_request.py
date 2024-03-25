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


class AccessTokenRequest(BaseModel):
    # id token
    id_token: str = Field(alias='idToken')

    # scope being requested
    scope: str = Field(alias='scope')

    # an existing token
    from_token: typing.Optional[str] = Field(None, alias='fromToken')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
