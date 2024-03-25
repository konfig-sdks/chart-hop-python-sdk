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

from chart_hop_python_sdk.pydantic.notification_job_data import NotificationJobData
from chart_hop_python_sdk.pydantic.notification_request_to_user_ids import NotificationRequestToUserIds

class NotificationRequest(BaseModel):
    # name of message template
    template_name: str = Field(alias='templateName')

    to_user_ids: NotificationRequestToUserIds = Field(alias='toUserIds')

    job_data: NotificationJobData = Field(alias='jobData')

    # name of the ATS system
    ats_name: typing.Optional[str] = Field(None, alias='atsName')

    # name of the organization
    org_name: typing.Optional[str] = Field(None, alias='orgName')

    # preferred name of the user
    user_name: typing.Optional[str] = Field(None, alias='userName')

    # summary of reason for email
    sync_summary: typing.Optional[str] = Field(None, alias='syncSummary')

    # id of the sync history process
    process_id: typing.Optional[str] = Field(None, alias='processId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
