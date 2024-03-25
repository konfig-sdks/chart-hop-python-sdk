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

from chart_hop_python_sdk.pydantic.cost_impact import CostImpact
from chart_hop_python_sdk.pydantic.results_access import ResultsAccess

class ScenarioMetadata(BaseModel):
    # scenario id
    scenario_id: str = Field(alias='scenarioId')

    # number of changes contained in scenario
    change_count: int = Field(alias='changeCount')

    # access information on the user for the entity
    access: typing.List[ResultsAccess] = Field(alias='access')

    # whether user can edit the scenario
    can_change: bool = Field(alias='canChange')

    cost: CostImpact = Field(alias='cost')

    # number of job changes contained in scenario
    job_count: typing.Optional[int] = Field(None, alias='jobCount')

    # most recent summary calculation ended at timestamp
    calc_end_at: typing.Optional[str] = Field(None, alias='calcEndAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
