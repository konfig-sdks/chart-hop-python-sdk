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

class PartialReportChart(BaseModel):
    # globally unique id
    id: typing.Optional[str] = Field(None, alias='id')

    # parent organization id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # parent report id
    report_id: typing.Optional[str] = Field(None, alias='reportId')

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

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
