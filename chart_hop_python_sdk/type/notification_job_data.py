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


class RequiredNotificationJobData(TypedDict):
    pass

class OptionalNotificationJobData(TypedDict, total=False):
    title: str

    jobId: str

    jobUrl: str

    jobProfileUrl: str

    atsJobUrl: str

    atsJobId: str

    atsJobReq: str

    atsJobReqField: str

    openJobsUrl: str

    department: str

    location: str

    manager: str

    backfill: str

    hireMgr: str

    recruiter: str

    recruitPriority: str

    recruit: str

    sensitive: str

    startDate: date

    estStartDate: date

    announceDate: date

    hireName: str

class NotificationJobData(RequiredNotificationJobData, OptionalNotificationJobData):
    pass
