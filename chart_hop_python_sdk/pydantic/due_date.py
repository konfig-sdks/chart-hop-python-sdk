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


class DueDate(BaseModel):
    type: Literal["EXACT", "RELATIVE"] = Field(alias='type')

    # due day, in either relative (-7d) or exact (YYYY-MM-DD) format
    due_day: str = Field(alias='dueDay')

    # due time, which is a LocalTime
    due_time: str = Field(alias='dueTime')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
