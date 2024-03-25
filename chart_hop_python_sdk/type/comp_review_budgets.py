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


class RequiredCompReviewBudgets(TypedDict):
    # How budgets are allocated
    allocationType: str

    # Whether all budget visualizations are visible or only those that apply to eligible employees in the reviewer's pod
    visualizationType: str

class OptionalCompReviewBudgets(TypedDict, total=False):
    pass

class CompReviewBudgets(RequiredCompReviewBudgets, OptionalCompReviewBudgets):
    pass
