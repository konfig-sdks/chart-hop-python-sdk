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

from chart_hop_python_sdk.pydantic.name import Name
from chart_hop_python_sdk.pydantic.user_list_row_group_ids import UserListRowGroupIds

class UserListRow(BaseModel):
    name: Name = Field(alias='name')

    invite_status: Literal["INVITED", "JOINED", "NOT_INVITED"] = Field(alias='inviteStatus')

    is_org_member: bool = Field(alias='isOrgMember')

    user_id: typing.Optional[str] = Field(None, alias='userId')

    person_id: typing.Optional[str] = Field(None, alias='personId')

    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    email: typing.Optional[str] = Field(None, alias='email')

    access: typing.Optional[str] = Field(None, alias='access')

    role_label: typing.Optional[str] = Field(None, alias='roleLabel')

    expr: typing.Optional[str] = Field(None, alias='expr')

    group_ids: typing.Optional[UserListRowGroupIds] = Field(None, alias='groupIds')

    login_at: typing.Optional[int] = Field(None, alias='loginAt')

    active_at: typing.Optional[int] = Field(None, alias='activeAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
