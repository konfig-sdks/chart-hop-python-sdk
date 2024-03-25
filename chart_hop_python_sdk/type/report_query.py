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

from chart_hop_python_sdk.type.report_filter import ReportFilter
from chart_hop_python_sdk.type.report_query_interval_dates import ReportQueryIntervalDates
from chart_hop_python_sdk.type.report_series_query import ReportSeriesQuery

class RequiredReportQuery(TypedDict):
    # options, including format, scenarioId, projectHires
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalReportQuery(TypedDict, total=False):
    # series to evaluate
    series: typing.List[ReportSeriesQuery]

    # filters to crosstab all results by (deprecated in reports V2, should use groupBy instead)
    filters: typing.List[ReportFilter]

    # content block to evaluate as a Carrot Template, as an alternative to using series
    content: str

    # start date, in either relative (-7d) or exact (YYYY-MM-DD) format
    startDate: str

    # end date, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    endDate: str

    # interval, if the query is a timeseries; if no interval, query is crosstabbed
    interval: str

    intervalDates: ReportQueryIntervalDates

class ReportQuery(RequiredReportQuery, OptionalReportQuery):
    pass
