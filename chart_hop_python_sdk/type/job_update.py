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

from chart_hop_python_sdk.type.comp import Comp
from chart_hop_python_sdk.type.group_assignment import GroupAssignment
from chart_hop_python_sdk.type.job_relationship import JobRelationship
from chart_hop_python_sdk.type.job_update_add_group_ids import JobUpdateAddGroupIds
from chart_hop_python_sdk.type.job_update_fields import JobUpdateFields
from chart_hop_python_sdk.type.job_update_remove_group_ids import JobUpdateRemoveGroupIds
from chart_hop_python_sdk.type.job_update_set_group_ids import JobUpdateSetGroupIds
from chart_hop_python_sdk.type.pair_string_object import PairStringObject
from chart_hop_python_sdk.type.stock_grant import StockGrant
from chart_hop_python_sdk.type.time_off import TimeOff

class RequiredJobUpdate(TypedDict):
    pass

class OptionalJobUpdate(TypedDict, total=False):
    # new title
    title: str

    # relationships to add
    addRelationships: typing.List[JobRelationship]

    # relationships to remove
    removeRelationships: typing.List[JobRelationship]

    addGroupIds: JobUpdateAddGroupIds

    removeGroupIds: JobUpdateRemoveGroupIds

    setGroupIds: JobUpdateSetGroupIds

    # group assignments to add
    addGroupAssignments: typing.List[GroupAssignment]

    # group assignments to remove
    removeGroupAssignments: typing.List[GroupAssignment]

    grant: StockGrant

    timeOff: TimeOff

    comp: Comp

    # new placement
    placement: str

    # new employment status
    employment: str

    # new view sensitivity
    sensitive: str

    # planned start date
    startDatePlanned: date

    # remove planned start date. if both startDatePlanned and startDatePlannedRemove are set, startDatePlanned takes precedence
    startDatePlannedRemove: bool

    # new expected start date - will update to person start date in future
    startDate: date

    # set who this job is backfilling
    backfillPersonId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # set who this job is backfilling
    hasUnsetFields: bool

    fields: JobUpdateFields

    # custom ordered fields values to set
    orderedFields: typing.List[PairStringObject]

class JobUpdate(RequiredJobUpdate, OptionalJobUpdate):
    pass
