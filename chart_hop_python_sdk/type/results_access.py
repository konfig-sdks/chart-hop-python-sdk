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

from chart_hop_python_sdk.type.access_action import AccessAction
from chart_hop_python_sdk.type.results_access_ids import ResultsAccessIds

class RequiredResultsAccess(TypedDict):
    allowed: typing.List[AccessAction]

class OptionalResultsAccess(TypedDict, total=False):
    ids: ResultsAccessIds

class ResultsAccess(RequiredResultsAccess, OptionalResultsAccess):
    pass
