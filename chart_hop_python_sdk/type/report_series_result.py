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

from chart_hop_python_sdk.type.label_color import LabelColor
from chart_hop_python_sdk.type.report_series_result_data import ReportSeriesResultData

class RequiredReportSeriesResult(TypedDict):
    # human-readable label for the series
    label: str

    # suggested color for the series
    color: str

    # number format (currently 'number', 'money', 'percent' allowed)
    format: str

    data: ReportSeriesResultData

    # true if the metric being returned is reporting on the entire interval (includes the intervalFrom or intervalUntil metric), false if just the last date in the interval
    isIntervalMetric: bool

class OptionalReportSeriesResult(TypedDict, total=False):
    xAxis: typing.List[LabelColor]

class ReportSeriesResult(RequiredReportSeriesResult, OptionalReportSeriesResult):
    pass
