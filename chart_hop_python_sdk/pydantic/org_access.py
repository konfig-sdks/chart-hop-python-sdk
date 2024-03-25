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

from chart_hop_python_sdk.pydantic.org_access_group_ids import OrgAccessGroupIds

class OrgAccess(BaseModel):
    # org id
    org_id: str = Field(alias='orgId')

    # legacy access permission level
    access: Literal["NONE", "VIEW", "LIMITED", "MEMBER_LIMITED_COMP", "MEMBER", "CUSTOM", "TECH_OWNER", "TIMEOFF", "CONTACT", "COMP_CASH", "COMP_EQUITY", "COMP_ALL", "RECRUIT_SENSITIVE", "RECRUIT_PRIMARY", "SENSITIVE_LIMITED_COMP", "SENSITIVE", "PRIMARY", "PEOPLE_OPS_ADMIN", "PEOPLE_OPS_ADMIN_NO_COMP_DATA", "PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA", "OWNER"] = Field(alias='access')

    # person id, if this user directly corresponds with a person
    person_id: typing.Optional[str] = Field(None, alias='personId')

    group_ids: typing.Optional[OrgAccessGroupIds] = Field(None, alias='groupIds')

    # expression that the above access applies to
    expr: typing.Optional[str] = Field(None, alias='expr')

    # timestamp that this org access will expire
    expire_at: typing.Optional[str] = Field(None, alias='expireAt')

    # the role id that defines the users access
    role_id: typing.Optional[str] = Field(None, alias='roleId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
