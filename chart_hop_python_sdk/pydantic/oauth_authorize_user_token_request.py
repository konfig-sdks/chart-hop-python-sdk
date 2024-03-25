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


class OauthAuthorizeUserTokenRequest(BaseModel):
    # Type of grant; 'password', 'refresh_token', 'authorization_code' supported
    grant_type: typing.Optional[str] = Field(None, alias='grant_type')

    # Username to authenticate
    username: typing.Optional[str] = Field(None, alias='username')

    # Password to authenticate
    password: typing.Optional[str] = Field(None, alias='password')

    # Requested access scope or scopes (space separated)
    scope: typing.Optional[str] = Field(None, alias='scope')

    # Authorization code
    code: typing.Optional[str] = Field(None, alias='code')

    # Redirect URI
    redirect_uri: typing.Optional[str] = Field(None, alias='redirect_uri')

    # Client id
    client_id: typing.Optional[str] = Field(None, alias='client_id')

    # Refresh token
    refresh_token: typing.Optional[str] = Field(None, alias='refresh_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
