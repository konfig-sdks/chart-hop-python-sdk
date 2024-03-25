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

from chart_hop_python_sdk.type.process import Process

class RequiredResultsProcess(TypedDict):
    data: typing.List[Process]

class OptionalResultsProcess(TypedDict, total=False):
    next: str

class ResultsProcess(RequiredResultsProcess, OptionalResultsProcess):
    pass
