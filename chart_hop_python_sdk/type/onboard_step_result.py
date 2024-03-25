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


class RequiredOnboardStepResult(TypedDict):
    # name of the step completed or skipped
    name: str

    # status of the step - either completed or skipped
    status: str

class OptionalOnboardStepResult(TypedDict, total=False):
    pass

class OnboardStepResult(RequiredOnboardStepResult, OptionalOnboardStepResult):
    pass
