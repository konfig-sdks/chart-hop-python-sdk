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

from chart_hop_python_sdk.pydantic.report_chart_ids import ReportChartIds
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class Report(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # report label
    label: str = Field(alias='label')

    # sharing settings of report
    share: Literal["NORMAL", "FULL"] = Field(alias='share')

    # sensitivity level of report
    sensitive: Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"] = Field(alias='sensitive')

    # users who are specifically granted permission to view or edit this report
    share_access: typing.List[ShareAccess] = Field(alias='shareAccess')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # last updated by user id
    update_id: str = Field(alias='updateId')

    # last updated timestamp
    update_at: str = Field(alias='updateAt')

    # report description
    description: typing.Optional[str] = Field(None, alias='description')

    # filter automatically applied to every chart in this report
    filter: typing.Optional[str] = Field(None, alias='filter')

    chart_ids: typing.Optional[ReportChartIds] = Field(None, alias='chartIds')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
