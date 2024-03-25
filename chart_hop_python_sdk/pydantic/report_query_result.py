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

from chart_hop_python_sdk.pydantic.report_date_interval import ReportDateInterval
from chart_hop_python_sdk.pydantic.report_group_by_dimension import ReportGroupByDimension
from chart_hop_python_sdk.pydantic.report_series_result import ReportSeriesResult

class ReportQueryResult(BaseModel):
    # list of series results
    series: typing.List[ReportSeriesResult] = Field(alias='series')

    # version used to generate the results
    version: typing.Optional[int] = Field(None, alias='version')

    # the results of rendering the content block, if a content template was used in the query
    content: typing.Optional[str] = Field(None, alias='content')

    # list of group-by dimensions with default values
    group_bys: typing.Optional[typing.List[ReportGroupByDimension]] = Field(None, alias='groupBys')

    # list of group-by dimensions with default values
    date_intervals: typing.Optional[typing.List[ReportDateInterval]] = Field(None, alias='dateIntervals')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
