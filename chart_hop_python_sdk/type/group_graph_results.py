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

from chart_hop_python_sdk.type.group_graph_result import GroupGraphResult

class RequiredGroupGraphResults(TypedDict):
    data: typing.List[GroupGraphResult]

class OptionalGroupGraphResults(TypedDict, total=False):
    nextId: str

class GroupGraphResults(RequiredGroupGraphResults, OptionalGroupGraphResults):
    pass
