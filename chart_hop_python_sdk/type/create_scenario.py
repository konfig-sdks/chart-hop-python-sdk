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

from chart_hop_python_sdk.type.create_scenario_valid_job_id_set import CreateScenarioValidJobIdSet
from chart_hop_python_sdk.type.money import Money
from chart_hop_python_sdk.type.scenario_shared_view_config import ScenarioSharedViewConfig
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredCreateScenario(TypedDict):
    # scenario name
    name: str

class OptionalCreateScenario(TypedDict, total=False):
    # scenario description
    description: str

    # date that this scenario diverges from primary
    startDate: str

    # status of scenario
    status: str

    # users who are specifically granted permission to this scenario
    shareAccess: typing.List[ShareAccess]

    # Type of scenario to be created
    type: str

    # whether or not the start date should stay fixed in time, or update to today's date as time passes
    startDateFixed: str

    # Query for selecting which people/jobs are initially included in the scenario (only applies to promotion scenarios)
    query: str

    validJobIdSet: CreateScenarioValidJobIdSet

    # The entity this scenario is associated with
    entityId: str

    # The type of entity associated with this scenario
    entityType: str

    # View configurations associated with this scenario
    sharedViewConfig: typing.List[ScenarioSharedViewConfig]

    budget: Money

    # CQL used to calculate the budget allocation in the scenario
    costCalc: str

class CreateScenario(RequiredCreateScenario, OptionalCreateScenario):
    pass
