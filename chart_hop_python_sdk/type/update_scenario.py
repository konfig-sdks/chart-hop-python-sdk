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

from chart_hop_python_sdk.type.money import Money
from chart_hop_python_sdk.type.scenario_shared_view_config import ScenarioSharedViewConfig
from chart_hop_python_sdk.type.share_access import ShareAccess
from chart_hop_python_sdk.type.update_scenario_valid_job_id_set import UpdateScenarioValidJobIdSet

class RequiredUpdateScenario(TypedDict):
    pass

class OptionalUpdateScenario(TypedDict, total=False):
    # scenario description
    description: str

    # scenario name
    name: str

    # date that this scenario diverges from primary
    startDate: str

    # status of scenario
    status: str

    # users who are specifically granted permission to this scenario
    shareAccess: typing.List[ShareAccess]

    # whether or not the start date should stay fixed in time, or update to today's date as time passes
    startDateFixed: str

    validJobIdSet: UpdateScenarioValidJobIdSet

    # The entity this scenario is associated with
    entityId: str

    # The type of entity associated with this scenario
    entityType: str

    # View configurations associated with this scenario
    sharedViewConfig: typing.List[ScenarioSharedViewConfig]

    budget: Money

    # CQL used to calculate the budget allocation in the scenario
    costCalc: str

class UpdateScenario(RequiredUpdateScenario, OptionalUpdateScenario):
    pass
