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


class NotificationJobData(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    job_id: typing.Optional[str] = Field(None, alias='jobId')

    job_url: typing.Optional[str] = Field(None, alias='jobUrl')

    job_profile_url: typing.Optional[str] = Field(None, alias='jobProfileUrl')

    ats_job_url: typing.Optional[str] = Field(None, alias='atsJobUrl')

    ats_job_id: typing.Optional[str] = Field(None, alias='atsJobId')

    ats_job_req: typing.Optional[str] = Field(None, alias='atsJobReq')

    ats_job_req_field: typing.Optional[str] = Field(None, alias='atsJobReqField')

    open_jobs_url: typing.Optional[str] = Field(None, alias='openJobsUrl')

    department: typing.Optional[str] = Field(None, alias='department')

    location: typing.Optional[str] = Field(None, alias='location')

    manager: typing.Optional[str] = Field(None, alias='manager')

    backfill: typing.Optional[str] = Field(None, alias='backfill')

    hire_mgr: typing.Optional[str] = Field(None, alias='hireMgr')

    recruiter: typing.Optional[str] = Field(None, alias='recruiter')

    recruit_priority: typing.Optional[str] = Field(None, alias='recruitPriority')

    recruit: typing.Optional[str] = Field(None, alias='recruit')

    sensitive: typing.Optional[str] = Field(None, alias='sensitive')

    start_date: typing.Optional[date] = Field(None, alias='startDate')

    est_start_date: typing.Optional[date] = Field(None, alias='estStartDate')

    announce_date: typing.Optional[date] = Field(None, alias='announceDate')

    hire_name: typing.Optional[str] = Field(None, alias='hireName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
