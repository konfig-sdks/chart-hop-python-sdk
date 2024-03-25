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

from chart_hop_python_sdk.pydantic.report_metrics_return_type_metric_collection import ReportMetricsReturnTypeMetricCollection
from chart_hop_python_sdk.pydantic.report_result import ReportResult

class ReportMetricsReturnType(BaseModel):
    result: ReportResult = Field(alias='result')

    metric_collection: ReportMetricsReturnTypeMetricCollection = Field(alias='metricCollection')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
