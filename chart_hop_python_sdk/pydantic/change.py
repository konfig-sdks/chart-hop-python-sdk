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

from chart_hop_python_sdk.pydantic.change_refs import ChangeRefs
from chart_hop_python_sdk.pydantic.job_update import JobUpdate
from chart_hop_python_sdk.pydantic.partial_job import PartialJob
from chart_hop_python_sdk.pydantic.upcoming_change import UpcomingChange

class Change(BaseModel):
    # unique id
    id: str = Field(alias='id')

    # job id
    job_id: str = Field(alias='jobId')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # type of change
    type: Literal["HIRE", "DEPART", "MOVE", "UPCOMING", "CREATE", "UPDATE", "DATA", "DELETE", "RELATE", "BACKFILL"] = Field(alias='type')

    # date of change
    date: date = Field(alias='date')

    # whether the change is active or not
    status: Literal["ACTIVE", "STRUCK", "CONFLICT", "INACTIVE", "PROPOSED"] = Field(alias='status')

    # scenario that this change belongs to
    scenario_id: typing.Optional[str] = Field(None, alias='scenarioId')

    # scenario that this change was merged in from, if the change originally came from a scenario
    merge_scenario_id: typing.Optional[str] = Field(None, alias='mergeScenarioId')

    # change that this change emanates from
    parent_change_id: typing.Optional[str] = Field(None, alias='parentChangeId')

    # connects this change to a previous version if itself that you might want to roll back to because of bad edits
    prior_state_change_id: typing.Optional[str] = Field(None, alias='priorStateChangeId')

    # sort order of change
    sort: typing.Optional[int] = Field(None, alias='sort')

    # for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change
    announce_date: typing.Optional[date] = Field(None, alias='announceDate')

    # the id of the person involved, or empty if no person attached to job
    person_id: typing.Optional[str] = Field(None, alias='personId')

    # for MOVE changes, the id of the job moving from; for RELATE changes, the id of the other job
    other_job_id: typing.Optional[str] = Field(None, alias='otherJobId')

    # for MOVE changes, the id of the other person involved in the move
    other_person_id: typing.Optional[str] = Field(None, alias='otherPersonId')

    # for DEPART changes, the type of departure
    depart_type: typing.Optional[Literal["VOLUNTARY", "INVOLUNTARY"]] = Field(None, alias='departType')

    # for DEPART changes, whether the departure was regrettable
    depart_regret: typing.Optional[Literal["REGRET", "NONREGRET"]] = Field(None, alias='departRegret')

    # if it's a promotion or a demotion
    promotion_type: typing.Optional[Literal["PROMOTION", "DEMOTION", "NONE"]] = Field(None, alias='promotionType')

    # the reason for the change
    reason: typing.Optional[str] = Field(None, alias='reason')

    # for RELATE changes, the type of the relationship
    relate_type: typing.Optional[Literal["MANAGER", "DIRECT", "INDIRECT_MANAGER", "INDIRECT", "NONE"]] = Field(None, alias='relateType')

    refs: typing.Optional[ChangeRefs] = Field(None, alias='refs')

    job: typing.Optional[PartialJob] = Field(None, alias='job')

    other_job: typing.Optional[PartialJob] = Field(None, alias='otherJob')

    # if this change was data submitted by a form, the id of that form
    form_id: typing.Optional[str] = Field(None, alias='formId')

    # if this change is associated with a assessment, the id of that assessment
    assessment_id: typing.Optional[str] = Field(None, alias='assessmentId')

    update: typing.Optional[JobUpdate] = Field(None, alias='update')

    upcoming: typing.Optional[UpcomingChange] = Field(None, alias='items')

    # for changes that have been struck due to a merge conflict, the description of the conflict
    conflict: typing.Optional[str] = Field(None, alias='conflict')

    # note on the change
    note: typing.Optional[str] = Field(None, alias='note')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # merged by user id, if this change was merged
    merge_id: typing.Optional[str] = Field(None, alias='mergeId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # timestamp of status change
    status_at: typing.Optional[str] = Field(None, alias='statusAt')

    # timestamp of approval
    approval_at: typing.Optional[str] = Field(None, alias='approvalAt')

    # approved by user id
    approval_id: typing.Optional[str] = Field(None, alias='approvalId')

    # approval/rejection note
    approval_note: typing.Optional[str] = Field(None, alias='approvalNote')

    # if approval is required, who is allowed to approve
    approval: typing.Optional[Literal["MANAGER", "GRAND_MANAGER"]] = Field(None, alias='approval')

    # view sensitivity for the author author of this form - the level of view access required to view the createId and updateId fields
    author_sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='authorSensitive')

    # flag indicating whether authorized user can modify this change (will vary depending on user)
    can_edit: typing.Optional[bool] = Field(None, alias='canEdit')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
