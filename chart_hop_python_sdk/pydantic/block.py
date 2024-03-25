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

from chart_hop_python_sdk.pydantic.block_fields import BlockFields

class Block(BaseModel):
    # human readable label for this block
    label: typing.Optional[str] = Field(None, alias='label')

    # filter condition expression applied to this block, used to determine whether the content appears on the target or not
    target_filter: typing.Optional[str] = Field(None, alias='targetFilter')

    # filter condition expression applied to this block, relative to the viewer
    read_filter: typing.Optional[str] = Field(None, alias='readFilter')

    fields: typing.Optional[BlockFields] = Field(None, alias='fields')

    # template content returned in this block
    content: typing.Optional[str] = Field(None, alias='content')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
