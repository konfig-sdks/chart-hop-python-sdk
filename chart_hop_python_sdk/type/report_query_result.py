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

from chart_hop_python_sdk.type.report_date_interval import ReportDateInterval
from chart_hop_python_sdk.type.report_group_by_dimension import ReportGroupByDimension
from chart_hop_python_sdk.type.report_series_result import ReportSeriesResult

class RequiredReportQueryResult(TypedDict):
    # list of series results
    series: typing.List[ReportSeriesResult]

class OptionalReportQueryResult(TypedDict, total=False):
    # version used to generate the results
    version: int

    # the results of rendering the content block, if a content template was used in the query
    content: str

    # list of group-by dimensions with default values
    groupBys: typing.List[ReportGroupByDimension]

    # list of group-by dimensions with default values
    dateIntervals: typing.List[ReportDateInterval]

class ReportQueryResult(RequiredReportQueryResult, OptionalReportQueryResult):
    pass
