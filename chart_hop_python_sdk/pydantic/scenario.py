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
from chart_hop_python_sdk.pydantic.money import Money
from chart_hop_python_sdk.pydantic.scenario_change_counts import ScenarioChangeCounts
from chart_hop_python_sdk.pydantic.scenario_shared_view_config import ScenarioSharedViewConfig
from chart_hop_python_sdk.pydantic.scenario_valid_job_id_set import ScenarioValidJobIdSet
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class Scenario(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # scenario name
    name: str = Field(alias='name')

    # date that this scenario diverges from primary
    start_date: str = Field(alias='startDate')

    # status of scenario
    status: Literal["OPEN", "INACTIVE", "MERGED", "DRAFT", "ARCHIVED"] = Field(alias='status')

    # users who are specifically granted permission to this scenario
    share_access: typing.List[ShareAccess] = Field(alias='shareAccess')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # last updated by user id
    update_id: str = Field(alias='updateId')

    # last updated timestamp
    update_at: str = Field(alias='updateAt')

    # scenario description
    description: typing.Optional[str] = Field(None, alias='description')

    cost: typing.Optional[CostImpact] = Field(None, alias='cost')

    # number of changes contained in scenario
    change_count: typing.Optional[int] = Field(None, alias='changeCount')

    change_counts: typing.Optional[ScenarioChangeCounts] = Field(None, alias='changeCounts')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    # merged by user id
    merge_id: typing.Optional[str] = Field(None, alias='mergeId')

    # merged timestamp
    merge_at: typing.Optional[str] = Field(None, alias='mergeAt')

    # most recent summary calculation started at timestamp
    calc_start_at: typing.Optional[str] = Field(None, alias='calcStartAt')

    # most recent summary calculation ended at timestamp
    calc_end_at: typing.Optional[str] = Field(None, alias='calcEndAt')

    # timestamp of most recent changes made to scenario
    change_at: typing.Optional[str] = Field(None, alias='changeAt')

    # user who made the most recent change to scenario
    change_id: typing.Optional[str] = Field(None, alias='changeId')

    # Type of scenario to be created
    type: typing.Optional[Literal["GENERAL", "COMP", "PROMOTION", "TERMINATE", "CREATE_JOB", "UPDATE_JOB", "BUDGET"]] = Field(None, alias='type')

    # whether or not the start date should stay fixed in time, or update to today's date as time passes
    start_date_fixed: typing.Optional[Literal["FIXED", "TODAY"]] = Field(None, alias='startDateFixed')

    # Query for selecting which people/jobs are initially included in the scenario (only applies to promotion scenarios)
    query: typing.Optional[str] = Field(None, alias='query')

    valid_job_id_set: typing.Optional[ScenarioValidJobIdSet] = Field(None, alias='validJobIdSet')

    # Approval request id, if the scenario has been submitted for approval
    approval_request_id: typing.Optional[str] = Field(None, alias='approvalRequestId')

    # The entity this scenario is associated with
    entity_id: typing.Optional[str] = Field(None, alias='entityId')

    # The type of entity associated with this scenario
    entity_type: typing.Optional[Literal["COMP_REVIEW"]] = Field(None, alias='entityType')

    # View configurations associated with this scenario
    shared_view_config: typing.Optional[typing.List[ScenarioSharedViewConfig]] = Field(None, alias='sharedViewConfig')

    budget: typing.Optional[Money] = Field(None, alias='budget')

    # CQL used to calculate the budget allocation in the scenario
    cost_calc: typing.Optional[str] = Field(None, alias='costCalc')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
