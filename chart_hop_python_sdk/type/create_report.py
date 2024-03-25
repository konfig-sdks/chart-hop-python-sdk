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

from chart_hop_python_sdk.type.create_report_chart_ids import CreateReportChartIds
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredCreateReport(TypedDict):
    # report label
    label: str

class OptionalCreateReport(TypedDict, total=False):
    # report description
    description: str

    # filter automatically applied to every chart in this report
    filter: str

    # sharing settings of report
    share: str

    # sensitivity level of report
    sensitive: str

    # users who are specifically granted permission to view or edit this report
    shareAccess: typing.List[ShareAccess]

    chartIds: CreateReportChartIds

class CreateReport(RequiredCreateReport, OptionalCreateReport):
    pass
