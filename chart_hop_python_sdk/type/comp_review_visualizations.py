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

from chart_hop_python_sdk.type.budget_calculation import BudgetCalculation
from chart_hop_python_sdk.type.comp_review_visualizations_job_to_base_spend_map import CompReviewVisualizationsJobToBaseSpendMap
from chart_hop_python_sdk.type.raise_percentage_histogram import RaisePercentageHistogram

class RequiredCompReviewVisualizations(TypedDict):
    raisePercentageHistogram: RaisePercentageHistogram

    jobToBaseSpendMap: CompReviewVisualizationsJobToBaseSpendMap

class OptionalCompReviewVisualizations(TypedDict, total=False):
    budgetPoolCalculation: BudgetCalculation

class CompReviewVisualizations(RequiredCompReviewVisualizations, OptionalCompReviewVisualizations):
    pass
