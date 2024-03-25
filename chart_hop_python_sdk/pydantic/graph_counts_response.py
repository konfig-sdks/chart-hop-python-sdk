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

from chart_hop_python_sdk.pydantic.graph_counts_response_counts import GraphCountsResponseCounts
from chart_hop_python_sdk.pydantic.graph_counts_response_job_to_manager_map import GraphCountsResponseJobToManagerMap
from chart_hop_python_sdk.pydantic.graph_counts_response_manager_to_job_map import GraphCountsResponseManagerToJobMap

class GraphCountsResponse(BaseModel):
    counts: GraphCountsResponseCounts = Field(alias='counts')

    manager_to_job_map: GraphCountsResponseManagerToJobMap = Field(alias='managerToJobMap')

    job_to_manager_map: GraphCountsResponseJobToManagerMap = Field(alias='jobToManagerMap')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
