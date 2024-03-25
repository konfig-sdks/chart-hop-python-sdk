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

from chart_hop_python_sdk.type.cost_impact import CostImpact
from chart_hop_python_sdk.type.results_access import ResultsAccess

class RequiredScenarioMetadata(TypedDict):
    # scenario id
    scenarioId: str

    # number of changes contained in scenario
    changeCount: int

    # access information on the user for the entity
    access: typing.List[ResultsAccess]

    # whether user can edit the scenario
    canChange: bool

    cost: CostImpact

class OptionalScenarioMetadata(TypedDict, total=False):
    # number of job changes contained in scenario
    jobCount: int

    # most recent summary calculation ended at timestamp
    calcEndAt: str

class ScenarioMetadata(RequiredScenarioMetadata, OptionalScenarioMetadata):
    pass
