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


class ViewAsRequest(BaseModel):
    # org id
    org_id: str = Field(alias='orgId')

    # scope being requested
    scope: str = Field(alias='scope')

    # person id
    person_id: typing.Optional[str] = Field(None, alias='personId')

    # user id
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # role id
    role_id: typing.Optional[str] = Field(None, alias='roleId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
