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

from chart_hop_python_sdk.type.report_metrics_return_type_metric_collection import ReportMetricsReturnTypeMetricCollection
from chart_hop_python_sdk.type.report_result import ReportResult

class RequiredReportMetricsReturnType(TypedDict):
    result: ReportResult

    metricCollection: ReportMetricsReturnTypeMetricCollection

class OptionalReportMetricsReturnType(TypedDict, total=False):
    pass

class ReportMetricsReturnType(RequiredReportMetricsReturnType, OptionalReportMetricsReturnType):
    pass
