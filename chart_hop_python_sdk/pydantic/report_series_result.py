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

from chart_hop_python_sdk.pydantic.label_color import LabelColor
from chart_hop_python_sdk.pydantic.report_series_result_data import ReportSeriesResultData

class ReportSeriesResult(BaseModel):
    # human-readable label for the series
    label: str = Field(alias='label')

    # suggested color for the series
    color: str = Field(alias='color')

    # number format (currently 'number', 'money', 'percent' allowed)
    format: str = Field(alias='format')

    data: ReportSeriesResultData = Field(alias='data')

    # true if the metric being returned is reporting on the entire interval (includes the intervalFrom or intervalUntil metric), false if just the last date in the interval
    is_interval_metric: bool = Field(alias='isIntervalMetric')

    x_axis: typing.Optional[typing.List[LabelColor]] = Field(None, alias='xAxis')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
