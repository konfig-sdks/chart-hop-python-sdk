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

from chart_hop_python_sdk.pydantic.policy_rule import PolicyRule
from chart_hop_python_sdk.pydantic.role import Role
from chart_hop_python_sdk.pydantic.user import User

class Policy(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # human-readable full name of policy
    label: str = Field(alias='label')

    # description of policy
    description: typing.Optional[str] = Field(None, alias='description')

    # parent organization id (empty if global)
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # the rules that define the policy
    rules: typing.Optional[typing.List[PolicyRule]] = Field(None, alias='rules')

    # the roles the policy is attached to
    roles: typing.Optional['typing.List[Role]'] = Field(None, alias='roles')

    # the users the policy is attached to
    users: typing.Optional[typing.List[User]] = Field(None, alias='users')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )