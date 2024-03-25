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

from chart_hop_python_sdk.pydantic.comp import Comp
from chart_hop_python_sdk.pydantic.group_assignment import GroupAssignment
from chart_hop_python_sdk.pydantic.job_relationship import JobRelationship
from chart_hop_python_sdk.pydantic.job_update_add_group_ids import JobUpdateAddGroupIds
from chart_hop_python_sdk.pydantic.job_update_fields import JobUpdateFields
from chart_hop_python_sdk.pydantic.job_update_remove_group_ids import JobUpdateRemoveGroupIds
from chart_hop_python_sdk.pydantic.job_update_set_group_ids import JobUpdateSetGroupIds
from chart_hop_python_sdk.pydantic.pair_string_object import PairStringObject
from chart_hop_python_sdk.pydantic.stock_grant import StockGrant
from chart_hop_python_sdk.pydantic.time_off import TimeOff

class JobUpdate(BaseModel):
    # new title
    title: typing.Optional[str] = Field(None, alias='title')

    # relationships to add
    add_relationships: typing.Optional[typing.List[JobRelationship]] = Field(None, alias='addRelationships')

    # relationships to remove
    remove_relationships: typing.Optional[typing.List[JobRelationship]] = Field(None, alias='removeRelationships')

    add_group_ids: typing.Optional[JobUpdateAddGroupIds] = Field(None, alias='addGroupIds')

    remove_group_ids: typing.Optional[JobUpdateRemoveGroupIds] = Field(None, alias='removeGroupIds')

    set_group_ids: typing.Optional[JobUpdateSetGroupIds] = Field(None, alias='setGroupIds')

    # group assignments to add
    add_group_assignments: typing.Optional[typing.List[GroupAssignment]] = Field(None, alias='addGroupAssignments')

    # group assignments to remove
    remove_group_assignments: typing.Optional[typing.List[GroupAssignment]] = Field(None, alias='removeGroupAssignments')

    grant: typing.Optional[StockGrant] = Field(None, alias='grant')

    time_off: typing.Optional[TimeOff] = Field(None, alias='timeOff')

    comp: typing.Optional[Comp] = Field(None, alias='comp')

    # new placement
    placement: typing.Optional[Literal["NORMAL", "ASSISTANT"]] = Field(None, alias='placement')

    # new employment status
    employment: typing.Optional[Literal["FULL", "PART", "TEMP", "CONTRACT", "INTERN", "EXPAT"]] = Field(None, alias='employment')

    # new view sensitivity
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # planned start date
    start_date_planned: typing.Optional[date] = Field(None, alias='startDatePlanned')

    # remove planned start date. if both startDatePlanned and startDatePlannedRemove are set, startDatePlanned takes precedence
    start_date_planned_remove: typing.Optional[bool] = Field(None, alias='startDatePlannedRemove')

    # new expected start date - will update to person start date in future
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    # set who this job is backfilling
    backfill_person_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='backfillPersonId')

    # set who this job is backfilling
    has_unset_fields: typing.Optional[bool] = Field(None, alias='hasUnsetFields')

    fields: typing.Optional[JobUpdateFields] = Field(None, alias='fields')

    # custom ordered fields values to set
    ordered_fields: typing.Optional[typing.List[PairStringObject]] = Field(None, alias='orderedFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
