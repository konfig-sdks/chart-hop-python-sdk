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

from chart_hop_python_sdk.type.report_query import ReportQuery

class RequiredCreateReportChart(TypedDict):
    # chart label
    label: str

    # chart type
    type: str

    query: ReportQuery

    # sort order
    sort: int

class OptionalCreateReportChart(TypedDict, total=False):
    # filter that applies to this chart
    filter: str

    # whether the chart filter overrides the global filter
    filterOverride: bool

    # whether the chart configuration is using advanced mode
    isAdvancedQueryMode: bool

class CreateReportChart(RequiredCreateReportChart, OptionalCreateReportChart):
    pass
