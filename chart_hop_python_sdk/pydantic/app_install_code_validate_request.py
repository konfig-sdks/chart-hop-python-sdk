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


class AppInstallCodeValidateRequest(BaseModel):
    # authorization code token value
    authorization_code: str = Field(alias='authorizationCode')

    # flag indicating if authorization code should be exchanged for an access token
    issue_access_token: bool = Field(alias='issueAccessToken')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
