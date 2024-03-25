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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.budget_calculation import BudgetCalculation
from chart_hop_python_sdk.pydantic.comp_review_visualizations_job_to_base_spend_map import CompReviewVisualizationsJobToBaseSpendMap
from chart_hop_python_sdk.pydantic.raise_percentage_histogram import RaisePercentageHistogram

class CompReviewVisualizations(BaseModel):
    raise_percentage_histogram: RaisePercentageHistogram = Field(alias='raisePercentageHistogram')

    job_to_base_spend_map: CompReviewVisualizationsJobToBaseSpendMap = Field(alias='jobToBaseSpendMap')

    budget_pool_calculation: typing.Optional[BudgetCalculation] = Field(None, alias='budgetPoolCalculation')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
