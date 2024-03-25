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

class CreateReportChart(BaseModel):
    # chart label
    label: str = Field(alias='label')

    # chart type
    type: Literal["LINE", "AREA", "STACKED", "BAR", "VERTICAL_BAR", "HORIZONTAL_BAR", "PIE", "TABLE", "TABLE_CROSSTAB", "SINGLE_METRIC", "HEADER", "TEXT"] = Field(alias='type')

    query: ReportQuery = Field(alias='query')

    # sort order
    sort: int = Field(alias='sort')

    # filter that applies to this chart
    filter: typing.Optional[str] = Field(None, alias='filter')

    # whether the chart filter overrides the global filter
    filter_override: typing.Optional[bool] = Field(None, alias='filterOverride')

    # whether the chart configuration is using advanced mode
    is_advanced_query_mode: typing.Optional[bool] = Field(None, alias='isAdvancedQueryMode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
