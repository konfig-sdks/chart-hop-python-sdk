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

from chart_hop_python_sdk.pydantic.group_graph_count import GroupGraphCount
from chart_hop_python_sdk.pydantic.group_graph_result_group import GroupGraphResultGroup
from chart_hop_python_sdk.pydantic.group_graph_result_group_positions import GroupGraphResultGroupPositions
from chart_hop_python_sdk.pydantic.group_graph_result_jobs import GroupGraphResultJobs
from chart_hop_python_sdk.pydantic.group_parent import GroupParent

class GroupGraphResult(BaseModel):
    group: GroupGraphResultGroup = Field(alias='group')

    jobs: GroupGraphResultJobs = Field(alias='jobs')

    group_positions: GroupGraphResultGroupPositions = Field(alias='groupPositions')

    under_count: GroupGraphCount = Field(alias='underCount')

    parent: typing.Optional[GroupParent] = Field(None, alias='parent')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
