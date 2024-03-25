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

class PartialPolicy(BaseModel):
    # description of policy
    description: typing.Optional[str] = Field(None, alias='description')

    # globally unique id
    id: typing.Optional[str] = Field(None, alias='id')

    # parent organization id (empty if global)
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # human-readable full name of policy
    label: typing.Optional[str] = Field(None, alias='label')

    # the rules that define the policy
    rules: typing.Optional[typing.List[PolicyRule]] = Field(None, alias='rules')

    # policy id that was copied (empty if original)
    copied_from_id: typing.Optional[str] = Field(None, alias='copiedFromId')

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
