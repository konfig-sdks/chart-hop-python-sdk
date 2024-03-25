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

from chart_hop_python_sdk.type.change import Change
from chart_hop_python_sdk.type.results_access import ResultsAccess

class RequiredResultsChange(TypedDict):
    data: typing.List[Change]

class OptionalResultsChange(TypedDict, total=False):
    next: str

    access: typing.List[ResultsAccess]

class ResultsChange(RequiredResultsChange, OptionalResultsChange):
    pass