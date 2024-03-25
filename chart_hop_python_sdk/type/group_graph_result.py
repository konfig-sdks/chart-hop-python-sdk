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

from chart_hop_python_sdk.type.group_graph_count import GroupGraphCount
from chart_hop_python_sdk.type.group_graph_result_group import GroupGraphResultGroup
from chart_hop_python_sdk.type.group_graph_result_group_positions import GroupGraphResultGroupPositions
from chart_hop_python_sdk.type.group_graph_result_jobs import GroupGraphResultJobs
from chart_hop_python_sdk.type.group_parent import GroupParent

class RequiredGroupGraphResult(TypedDict):
    group: GroupGraphResultGroup

    jobs: GroupGraphResultJobs

    groupPositions: GroupGraphResultGroupPositions

    underCount: GroupGraphCount

class OptionalGroupGraphResult(TypedDict, total=False):
    parent: GroupParent

class GroupGraphResult(RequiredGroupGraphResult, OptionalGroupGraphResult):
    pass
