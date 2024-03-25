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

from chart_hop_python_sdk.pydantic.money import Money
from chart_hop_python_sdk.pydantic.scenario_shared_view_config import ScenarioSharedViewConfig
from chart_hop_python_sdk.pydantic.share_access import ShareAccess
from chart_hop_python_sdk.pydantic.update_scenario_valid_job_id_set import UpdateScenarioValidJobIdSet

class UpdateScenario(BaseModel):
    # scenario description
    description: typing.Optional[str] = Field(None, alias='description')

    # scenario name
    name: typing.Optional[str] = Field(None, alias='name')

    # date that this scenario diverges from primary
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # status of scenario
    status: typing.Optional[Literal["OPEN", "INACTIVE", "MERGED", "DRAFT", "ARCHIVED"]] = Field(None, alias='status')

    # users who are specifically granted permission to this scenario
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # whether or not the start date should stay fixed in time, or update to today's date as time passes
    start_date_fixed: typing.Optional[Literal["FIXED", "TODAY"]] = Field(None, alias='startDateFixed')

    valid_job_id_set: typing.Optional[UpdateScenarioValidJobIdSet] = Field(None, alias='validJobIdSet')

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
