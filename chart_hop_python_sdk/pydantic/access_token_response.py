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


class AccessTokenResponse(BaseModel):
    # access token value
    access_token: str = Field(alias='access_token')

    # access token type
    token_type: str = Field(alias='token_type')

    # expiration time of token, in seconds
    expires_in: int = Field(alias='expires_in')

    # refresh token value
    refresh_token: typing.Optional[str] = Field(None, alias='refresh_token')

    # scope of the access token
    scope: typing.Optional[str] = Field(None, alias='scope')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
