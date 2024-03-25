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

from chart_hop_python_sdk.pydantic.report_query import ReportQuery

class UpdateReportChart(BaseModel):
    # chart label
    label: typing.Optional[str] = Field(None, alias='label')

    # chart type
    type: typing.Optional[Literal["LINE", "AREA", "STACKED", "BAR", "VERTICAL_BAR", "HORIZONTAL_BAR", "PIE", "TABLE", "TABLE_CROSSTAB", "SINGLE_METRIC", "HEADER", "TEXT"]] = Field(None, alias='type')

    # filter that applies to this chart
    filter: typing.Optional[str] = Field(None, alias='filter')

    # whether the chart filter overrides the global filter
    filter_override: typing.Optional[bool] = Field(None, alias='filterOverride')

    query: typing.Optional[ReportQuery] = Field(None, alias='query')

    # sort order
    sort: typing.Optional[int] = Field(None, alias='sort')

    # whether the chart configuration is using advanced mode
    is_advanced_query_mode: typing.Optional[bool] = Field(None, alias='isAdvancedQueryMode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
