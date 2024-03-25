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

class UpdateProfileTab(BaseModel):
    # human-readable name of profile tab
    label: typing.Optional[str] = Field(None, alias='label')

    # ordered list of blocks contained by profile tab
    blocks: typing.Optional[typing.List[Block]] = Field(None, alias='blocks')

    # status of the profile tab
    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    # filter that controls on which profiles this tab will appear
    target_filter: typing.Optional[str] = Field(None, alias='targetFilter')

    # filter that controls which viewers can read this profile tab. The profileTab:read permission, if present, overrides this filter
    read_filter: typing.Optional[str] = Field(None, alias='readFilter')

    # sort order
    sort: typing.Optional[int] = Field(None, alias='sort')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
