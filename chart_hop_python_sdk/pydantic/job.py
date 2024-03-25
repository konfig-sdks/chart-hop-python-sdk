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
from chart_hop_python_sdk.pydantic.job_fields import JobFields
from chart_hop_python_sdk.pydantic.job_group_ids import JobGroupIds
from chart_hop_python_sdk.pydantic.job_manager_ids import JobManagerIds
from chart_hop_python_sdk.pydantic.job_relationship import JobRelationship
from chart_hop_python_sdk.pydantic.upcoming_change import UpcomingChange

class Job(BaseModel):
    # job title
    title: str = Field(alias='title')

    # globally unique job id
    job_id: str = Field(alias='jobId')

    # parent organization id
    org_id: str = Field(alias='orgId')

    group_ids: JobGroupIds = Field(alias='groupIds')

    # tracked group assignments that this job is a member or lead of
    group_assignments: typing.List[GroupAssignment] = Field(alias='groupAssignments')

    fields: JobFields = Field(alias='fields')

    comp: typing.Optional[Comp] = Field(None, alias='comp')

    # view sensitive of the job while open
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # relationship to other jobs
    relationships: typing.Optional[typing.List[JobRelationship]] = Field(None, alias='relationships')

    manager_ids: typing.Optional[JobManagerIds] = Field(None, alias='managerIds')

    # guidance on placement
    placement: typing.Optional[Literal["NORMAL", "ASSISTANT"]] = Field(None, alias='placement')

    # employment status
    employment: typing.Optional[Literal["FULL", "PART", "TEMP", "CONTRACT", "INTERN", "EXPAT"]] = Field(None, alias='employment')

    # for empty jobs, expected start date - for filled jobs, confirmed start date
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    # expected start date whether job is open or has been filled - doesn't change when job is filled
    start_date_planned: typing.Optional[date] = Field(None, alias='startDatePlanned')

    # if personId is present, the first day of that person in the org after the latest departure (if any)
    person_start_date: typing.Optional[date] = Field(None, alias='personStartDate')

    # if personId is present and the person is departing, the last day of that person in the org
    person_end_date: typing.Optional[date] = Field(None, alias='personEndDate')

    # if personId is present, the first day of that person in the job
    person_job_start_date: typing.Optional[date] = Field(None, alias='personJobStartDate')

    # if personId is present and the person is departing or moving out, the last day of that person in the job
    person_job_end_date: typing.Optional[date] = Field(None, alias='personJobEndDate')

    # the person holding this job -- either currently in the job, or upcoming announced hire
    person_id: typing.Optional[str] = Field(None, alias='personId')

    # if a HIRE, MOVE, or DEPART are upcoming, the details on those changes - should only include id, type, date, announceDate, personId
    upcoming: typing.Optional[typing.List[UpcomingChange]] = Field(None, alias='upcoming')

    # scenario that the job was created in (null if job is on primary timeline)
    scenario_id: typing.Optional[str] = Field(None, alias='scenarioId')

    # the person who most recently held the job, who this represents a backfill for
    backfill_person_id: typing.Optional[str] = Field(None, alias='backfillPersonId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
