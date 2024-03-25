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

from chart_hop_python_sdk.pydantic.tracked_group_ref import TrackedGroupRef

class GroupAssignment(BaseModel):
    group: TrackedGroupRef = Field(alias='group')

    # the type of the assignment of the job to the group
    assignment_type: Literal["LEAD", "MEMBER"] = Field(alias='assignmentType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
