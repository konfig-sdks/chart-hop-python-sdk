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

from chart_hop_python_sdk.type.results_access import ResultsAccess
from chart_hop_python_sdk.type.results_change_data import ResultsChangeData
from chart_hop_python_sdk.type.scenario_changes_with_budget_rollup_budget_pool_summaries import ScenarioChangesWithBudgetRollupBudgetPoolSummaries

class RequiredScenarioChangesWithBudgetRollup(TypedDict):
    changes: ResultsChangeData

    budgetPoolSummaries: ScenarioChangesWithBudgetRollupBudgetPoolSummaries

class OptionalScenarioChangesWithBudgetRollup(TypedDict, total=False):
    access: typing.List[ResultsAccess]

class ScenarioChangesWithBudgetRollup(RequiredScenarioChangesWithBudgetRollup, OptionalScenarioChangesWithBudgetRollup):
    pass
