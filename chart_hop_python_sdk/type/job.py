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
from chart_hop_python_sdk.type.job_fields import JobFields
from chart_hop_python_sdk.type.job_group_ids import JobGroupIds
from chart_hop_python_sdk.type.job_manager_ids import JobManagerIds
from chart_hop_python_sdk.type.job_relationship import JobRelationship
from chart_hop_python_sdk.type.upcoming_change import UpcomingChange

class RequiredJob(TypedDict):
    # job title
    title: str

    # globally unique job id
    jobId: str

    # parent organization id
    orgId: str

    groupIds: JobGroupIds

    # tracked group assignments that this job is a member or lead of
    groupAssignments: typing.List[GroupAssignment]

    fields: JobFields

class OptionalJob(TypedDict, total=False):
    comp: Comp

    # view sensitive of the job while open
    sensitive: str

    # relationship to other jobs
    relationships: typing.List[JobRelationship]

    managerIds: JobManagerIds

    # guidance on placement
    placement: str

    # employment status
    employment: str

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

    # if personId is present and the person is departing or moving out, the last day of that person in the job
    personJobEndDate: date

    # the person holding this job -- either currently in the job, or upcoming announced hire
    personId: str

    # if a HIRE, MOVE, or DEPART are upcoming, the details on those changes - should only include id, type, date, announceDate, personId
    upcoming: typing.List[UpcomingChange]

    # scenario that the job was created in (null if job is on primary timeline)
    scenarioId: str

    # the person who most recently held the job, who this represents a backfill for
    backfillPersonId: str

class Job(RequiredJob, OptionalJob):
    pass
