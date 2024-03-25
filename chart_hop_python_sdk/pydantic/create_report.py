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

from chart_hop_python_sdk.pydantic.create_report_chart_ids import CreateReportChartIds
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class CreateReport(BaseModel):
    # report label
    label: str = Field(alias='label')

    # report description
    description: typing.Optional[str] = Field(None, alias='description')

    # filter automatically applied to every chart in this report
    filter: typing.Optional[str] = Field(None, alias='filter')

    # sharing settings of report
    share: typing.Optional[Literal["NORMAL", "FULL"]] = Field(None, alias='share')

    # sensitivity level of report
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # users who are specifically granted permission to view or edit this report
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    chart_ids: typing.Optional[CreateReportChartIds] = Field(None, alias='chartIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
