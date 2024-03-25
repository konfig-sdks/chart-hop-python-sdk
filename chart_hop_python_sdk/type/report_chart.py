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

class RequiredReportChart(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # chart label
    label: str

    query: ReportQuery

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalReportChart(TypedDict, total=False):
    # parent report id
    reportId: str

    # chart type
    type: str

    # filter that applies to this chart
    filter: str

    # whether the chart filter overrides the global filter
    filterOverride: bool

    # sort order
    sort: int

    # whether the chart configuration is using advanced mode
    isAdvancedQueryMode: bool

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class ReportChart(RequiredReportChart, OptionalReportChart):
    pass
