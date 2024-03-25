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


class RequiredOauthAuthorizeUserTokenRequest(TypedDict):
    pass

class OptionalOauthAuthorizeUserTokenRequest(TypedDict, total=False):
    # Type of grant; 'password', 'refresh_token', 'authorization_code' supported
    grant_type: str

    # Username to authenticate
    username: str

    # Password to authenticate
    password: str

    # Requested access scope or scopes (space separated)
    scope: str

    # Authorization code
    code: str

    # Redirect URI
    redirect_uri: str

    # Client id
    client_id: str

    # Refresh token
    refresh_token: str

class OauthAuthorizeUserTokenRequest(RequiredOauthAuthorizeUserTokenRequest, OptionalOauthAuthorizeUserTokenRequest):
    pass
