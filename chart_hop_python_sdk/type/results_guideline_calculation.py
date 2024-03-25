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

from chart_hop_python_sdk.type.guideline_calculation import GuidelineCalculation

class RequiredResultsGuidelineCalculation(TypedDict):
    data: typing.List[GuidelineCalculation]

class OptionalResultsGuidelineCalculation(TypedDict, total=False):
    next: str

class ResultsGuidelineCalculation(RequiredResultsGuidelineCalculation, OptionalResultsGuidelineCalculation):
    pass