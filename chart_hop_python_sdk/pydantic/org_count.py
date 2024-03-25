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


class OrgCount(BaseModel):
    job_count: int = Field(alias='jobCount')

    person_count: int = Field(alias='personCount')

    starting_count: int = Field(alias='startingCount')

    departing_count: int = Field(alias='departingCount')

    group_count: typing.Optional[int] = Field(None, alias='groupCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
