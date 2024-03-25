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

from chart_hop_python_sdk.type.change_refs import ChangeRefs
from chart_hop_python_sdk.type.job_update import JobUpdate
from chart_hop_python_sdk.type.partial_job import PartialJob
from chart_hop_python_sdk.type.upcoming_change import UpcomingChange

class RequiredChange(TypedDict):
    # unique id
    id: str

    # job id
    jobId: str

    # parent organization id
    orgId: str

    # type of change
    type: str

    # date of change
    date: date

    # whether the change is active or not
    status: str

class OptionalChange(TypedDict, total=False):
    # scenario that this change belongs to
    scenarioId: str

    # scenario that this change was merged in from, if the change originally came from a scenario
    mergeScenarioId: str

    # change that this change emanates from
    parentChangeId: str

    # connects this change to a previous version if itself that you might want to roll back to because of bad edits
    priorStateChangeId: str

    # sort order of change
    sort: int

    # for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change
    announceDate: date

    # the id of the person involved, or empty if no person attached to job
    personId: str

    # for MOVE changes, the id of the job moving from; for RELATE changes, the id of the other job
    otherJobId: str

    # for MOVE changes, the id of the other person involved in the move
    otherPersonId: str

    # for DEPART changes, the type of departure
    departType: str

    # for DEPART changes, whether the departure was regrettable
    departRegret: str

    # if it's a promotion or a demotion
    promotionType: str

    # the reason for the change
    reason: str

    # for RELATE changes, the type of the relationship
    relateType: str

    refs: ChangeRefs

    job: PartialJob

    otherJob: PartialJob

    # if this change was data submitted by a form, the id of that form
    formId: str

    # if this change is associated with a assessment, the id of that assessment
    assessmentId: str

    update: JobUpdate

    items: UpcomingChange

    # for changes that have been struck due to a merge conflict, the description of the conflict
    conflict: str

    # note on the change
    note: str

    # created by user id
    createId: str

    # merged by user id, if this change was merged
    mergeId: str

    # created timestamp
    createAt: str

    # updated timestamp
    updateAt: str

    # updated by user id
    updateId: str

    # timestamp of status change
    statusAt: str

    # timestamp of approval
    approvalAt: str

    # approved by user id
    approvalId: str

    # approval/rejection note
    approvalNote: str

    # if approval is required, who is allowed to approve
    approval: str

    # view sensitivity for the author author of this form - the level of view access required to view the createId and updateId fields
    authorSensitive: str

    # flag indicating whether authorized user can modify this change (will vary depending on user)
    canEdit: bool

class Change(RequiredChange, OptionalChange):
    pass
