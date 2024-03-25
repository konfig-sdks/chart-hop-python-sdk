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

from chart_hop_python_sdk.pydantic.partial_report_chart_ids import PartialReportChartIds
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class PartialReport(BaseModel):
    # report description
    description: typing.Optional[str] = Field(None, alias='description')

    # globally unique id
    id: typing.Optional[str] = Field(None, alias='id')

    # parent organization id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # report label
    label: typing.Optional[str] = Field(None, alias='label')

    # filter automatically applied to every chart in this report
    filter: typing.Optional[str] = Field(None, alias='filter')

    # sharing settings of report
    share: typing.Optional[Literal["NORMAL", "FULL"]] = Field(None, alias='share')

    # sensitivity level of report
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # users who are specifically granted permission to view or edit this report
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    chart_ids: typing.Optional[PartialReportChartIds] = Field(None, alias='chartIds')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
