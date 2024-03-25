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


class RequiredAccessTokenResponse(TypedDict):
    # access token value
    access_token: str

    # access token type
    token_type: str

    # expiration time of token, in seconds
    expires_in: int

class OptionalAccessTokenResponse(TypedDict, total=False):
    # refresh token value
    refresh_token: str

    # scope of the access token
    scope: str

class AccessTokenResponse(RequiredAccessTokenResponse, OptionalAccessTokenResponse):
    pass
