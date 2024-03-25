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


class GraphCount(BaseModel):
    under: int = Field(alias='under')

    sibling: int = Field(alias='sibling')

    under_unfilled: int = Field(alias='underUnfilled')

    sibling_unfilled: int = Field(alias='siblingUnfilled')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
