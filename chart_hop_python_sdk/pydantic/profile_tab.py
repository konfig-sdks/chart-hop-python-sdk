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

from chart_hop_python_sdk.pydantic.block import Block

class ProfileTab(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # human-readable name of profile tab
    label: str = Field(alias='label')

    # ordered list of blocks contained by profile tab
    blocks: typing.List[Block] = Field(alias='blocks')

    # status of the profile tab
    status: Literal["ACTIVE", "INACTIVE"] = Field(alias='status')

    # sort order
    sort: int = Field(alias='sort')

    # filter that controls on which profiles this tab will appear
    target_filter: typing.Optional[str] = Field(None, alias='targetFilter')

    # filter that controls which viewers can read this profile tab. The profileTab:read permission, if present, overrides this filter
    read_filter: typing.Optional[str] = Field(None, alias='readFilter')

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
