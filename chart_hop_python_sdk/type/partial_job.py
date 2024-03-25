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
from chart_hop_python_sdk.type.partial_job_field_dates import PartialJobFieldDates
from chart_hop_python_sdk.type.partial_job_fields import PartialJobFields
from chart_hop_python_sdk.type.partial_job_fields_proposed import PartialJobFieldsProposed
from chart_hop_python_sdk.type.partial_job_group_ids import PartialJobGroupIds
from chart_hop_python_sdk.type.upcoming_change import UpcomingChange

class RequiredPartialJob(TypedDict):
    pass

class OptionalPartialJob(TypedDict, total=False):
    # job title
    title: str

    # globally unique job id
    jobId: str

    # parent organization id
    orgId: str

    # snapshot that this job belongs to
    snapshotId: str

    comp: Comp

    # view sensitive of the job while open
    sensitive: str

    # relationship to other jobs
    relationships: typing.List[JobRelationship]

    groupIds: PartialJobGroupIds

    # tracked group assignments that this job is a member or lead of
    groupAssignments: typing.List[GroupAssignment]

    # guidance on placement
    placement: str

    # employment status
    employment: str

    # current state - whether the job is open, filled, or has someone departed or hired
    state: str

    fields: PartialJobFields

    fieldDates: PartialJobFieldDates

    fieldsProposed: PartialJobFieldsProposed

    # job creation date
    createDate: date

    # for empty jobs, expected start date - for filled jobs, confirmed start date
    startDate: date

    # expected start date whether job is open or has been filled - doesn't change when job is filled
    startDatePlanned: date

    # if personId is present, the first day of that person in the org after the latest departure (if any)
    personStartDate: date

    # if personId is present and the person is departing, the last day of that person in the org
    personEndDate: date

    # if personId is present, the first day of that person in the job
    personJobStartDate: date

    # if personId is present, the first day that the personId actually filled the job
    personIdDate: date

    # if personId is present and the person is departing or moving out, the last day of that person in the job
    personJobEndDate: date

    # the person holding this job -- either currently in the job, or upcoming announced hire
    personId: str

    # the person who most recently held the job, who this represents a backfill for
    backfillPersonId: str

    # another job which is planned to be a backfill for this job
    backfillByJobId: str

    # if a HIRE, MOVE, or DEPART are upcoming, the details on those changes - should only include id, type, date, announceDate, personId
    upcoming: typing.List[UpcomingChange]

    # scenario that the job was created in (null if job is on primary timeline)
    scenarioId: str

    # scenario that the job was changed in (null if job is on primary timeline)
    scenarioChangedId: str

class PartialJob(RequiredPartialJob, OptionalPartialJob):
    pass
