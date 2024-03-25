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
from chart_hop_python_sdk.type.money import Money
from chart_hop_python_sdk.type.scenario_change_counts import ScenarioChangeCounts
from chart_hop_python_sdk.type.scenario_shared_view_config import ScenarioSharedViewConfig
from chart_hop_python_sdk.type.scenario_valid_job_id_set import ScenarioValidJobIdSet
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredScenario(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # scenario name
    name: str

    # date that this scenario diverges from primary
    startDate: str

    # status of scenario
    status: str

    # users who are specifically granted permission to this scenario
    shareAccess: typing.List[ShareAccess]

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalScenario(TypedDict, total=False):
    # scenario description
    description: str

    cost: CostImpact

    # number of changes contained in scenario
    changeCount: int

    changeCounts: ScenarioChangeCounts

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

    # merged by user id
    mergeId: str

    # merged timestamp
    mergeAt: str

    # most recent summary calculation started at timestamp
    calcStartAt: str

    # most recent summary calculation ended at timestamp
    calcEndAt: str

    # timestamp of most recent changes made to scenario
    changeAt: str

    # user who made the most recent change to scenario
    changeId: str

    # Type of scenario to be created
    type: str

    # whether or not the start date should stay fixed in time, or update to today's date as time passes
    startDateFixed: str

    # Query for selecting which people/jobs are initially included in the scenario (only applies to promotion scenarios)
    query: str

    validJobIdSet: ScenarioValidJobIdSet

    # Approval request id, if the scenario has been submitted for approval
    approvalRequestId: str

    # The entity this scenario is associated with
    entityId: str

    # The type of entity associated with this scenario
    entityType: str

    # View configurations associated with this scenario
    sharedViewConfig: typing.List[ScenarioSharedViewConfig]

    budget: Money

    # CQL used to calculate the budget allocation in the scenario
    costCalc: str

class Scenario(RequiredScenario, OptionalScenario):
    pass
