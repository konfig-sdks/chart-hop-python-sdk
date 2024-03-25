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

from chart_hop_python_sdk.type.notification_job_data import NotificationJobData
from chart_hop_python_sdk.type.notification_request_to_user_ids import NotificationRequestToUserIds

class RequiredNotificationRequest(TypedDict):
    # name of message template
    templateName: str

    toUserIds: NotificationRequestToUserIds

    jobData: NotificationJobData

class OptionalNotificationRequest(TypedDict, total=False):
    # name of the ATS system
    atsName: str

    # name of the organization
    orgName: str

    # preferred name of the user
    userName: str

    # summary of reason for email
    syncSummary: str

    # id of the sync history process
    processId: str

class NotificationRequest(RequiredNotificationRequest, OptionalNotificationRequest):
    pass
