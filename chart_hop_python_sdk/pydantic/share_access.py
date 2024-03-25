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


class ShareAccess(BaseModel):
    # access permission level
    access: Literal["NONE", "LIMITED_READ", "LIMITED_WRITE", "STANDARD_READ", "STANDARD_WRITE", "COMPENSATION_READ", "FULL_READ", "COMP_PLANNING_PARTICIPANT", "COMPENSATION_WRITE", "WRITE", "COMPENSATION_OWNER", "OWNER"] = Field(alias='access')

    # user id
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # group id
    group_id: typing.Optional[str] = Field(None, alias='groupId')

    # fields
    fields: typing.Optional[str] = Field(None, alias='fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
