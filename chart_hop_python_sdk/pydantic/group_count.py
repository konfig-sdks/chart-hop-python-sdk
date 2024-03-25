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


class GroupCount(BaseModel):
    # total number of groups
    total_group_count: typing.Union[int, float] = Field(alias='totalGroupCount')

    # number of groups that are part of a larger group tree
    relationship_group_count: typing.Union[int, float] = Field(alias='relationshipGroupCount')

    # number of orphaned groups that do not belong to any group tree
    orphaned_group_count: typing.Union[int, float] = Field(alias='orphanedGroupCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
