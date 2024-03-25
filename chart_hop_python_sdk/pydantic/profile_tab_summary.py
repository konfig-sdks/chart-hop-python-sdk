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

class ProfileTabSummary(BaseModel):
    id: str = Field(alias='id')

    label: str = Field(alias='label')

    is_builtin: bool = Field(alias='isBuiltin')

    is_sensitive: typing.Optional[bool] = Field(None, alias='isSensitive')

    blocks: typing.Optional[typing.List[Block]] = Field(None, alias='blocks')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
