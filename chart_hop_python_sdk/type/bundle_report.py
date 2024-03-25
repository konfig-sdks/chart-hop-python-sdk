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

from chart_hop_python_sdk.type.partial_report import PartialReport
from chart_hop_python_sdk.type.partial_report_chart import PartialReportChart

class RequiredBundleReport(TypedDict):
    report: PartialReport

class OptionalBundleReport(TypedDict, total=False):
    # list of charts used in the report
    charts: typing.List[PartialReportChart]

class BundleReport(RequiredBundleReport, OptionalBundleReport):
    pass
