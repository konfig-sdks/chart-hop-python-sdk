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

from chart_hop_python_sdk.pydantic.partial_report import PartialReport
from chart_hop_python_sdk.pydantic.partial_report_chart import PartialReportChart

class BundleReport(BaseModel):
    report: PartialReport = Field(alias='report')

    # list of charts used in the report
    charts: typing.Optional[typing.List[PartialReportChart]] = Field(None, alias='charts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )