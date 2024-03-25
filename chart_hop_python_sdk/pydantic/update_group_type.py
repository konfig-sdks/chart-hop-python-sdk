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


class UpdateGroupType(BaseModel):
    # unique name of group
    name: typing.Optional[str] = Field(None, alias='name')

    # unique slug of group
    slug: typing.Optional[str] = Field(None, alias='slug')

    # whether the group requires members to be positions
    require_positions: typing.Optional[bool] = Field(None, alias='requirePositions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )