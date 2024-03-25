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

from chart_hop_python_sdk.pydantic.create_role_policy_ids import CreateRolePolicyIds

class CreateRole(BaseModel):
    # human-readable full name of role
    label: str = Field(alias='label')

    # description of role
    description: typing.Optional[str] = Field(None, alias='description')

    # parent organization id (empty if global)
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    policy_ids: typing.Optional[CreateRolePolicyIds] = Field(None, alias='policyIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
