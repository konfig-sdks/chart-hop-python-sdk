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

from chart_hop_python_sdk.type.graph_counts_response_counts import GraphCountsResponseCounts
from chart_hop_python_sdk.type.graph_counts_response_job_to_manager_map import GraphCountsResponseJobToManagerMap
from chart_hop_python_sdk.type.graph_counts_response_manager_to_job_map import GraphCountsResponseManagerToJobMap

class RequiredGraphCountsResponse(TypedDict):
    counts: GraphCountsResponseCounts

    managerToJobMap: GraphCountsResponseManagerToJobMap

    jobToManagerMap: GraphCountsResponseJobToManagerMap

class OptionalGraphCountsResponse(TypedDict, total=False):
    pass

class GraphCountsResponse(RequiredGraphCountsResponse, OptionalGraphCountsResponse):
    pass
