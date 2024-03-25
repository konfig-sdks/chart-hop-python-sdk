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

from chart_hop_python_sdk.pydantic.results_access import ResultsAccess
from chart_hop_python_sdk.pydantic.results_change_data import ResultsChangeData
from chart_hop_python_sdk.pydantic.scenario_changes_with_budget_rollup_budget_pool_summaries import ScenarioChangesWithBudgetRollupBudgetPoolSummaries

class ScenarioChangesWithBudgetRollup(BaseModel):
    changes: ResultsChangeData = Field(alias='changes')

    budget_pool_summaries: ScenarioChangesWithBudgetRollupBudgetPoolSummaries = Field(alias='budgetPoolSummaries')

    access: typing.Optional[typing.List[ResultsAccess]] = Field(None, alias='access')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
