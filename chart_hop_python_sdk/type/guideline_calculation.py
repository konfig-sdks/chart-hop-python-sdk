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

from chart_hop_python_sdk.type.deviation import Deviation
from chart_hop_python_sdk.type.guideline_calculation_fields import GuidelineCalculationFields

class RequiredGuidelineCalculation(TypedDict):
    guidelineId: str

    jobId: str

    compReviewId: str

    guidelineLabel: str

    appliedField: str

    flagMode: str

    isDeviated: bool

    deviation: Deviation

    fields: GuidelineCalculationFields

class OptionalGuidelineCalculation(TypedDict, total=False):
    budgetPoolId: str

    min: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    max: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    target: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    flagDeviationThreshold: typing.Union[int, float]

class GuidelineCalculation(RequiredGuidelineCalculation, OptionalGuidelineCalculation):
    pass
