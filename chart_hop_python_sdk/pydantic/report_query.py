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

from chart_hop_python_sdk.pydantic.report_filter import ReportFilter
from chart_hop_python_sdk.pydantic.report_query_interval_dates import ReportQueryIntervalDates
from chart_hop_python_sdk.pydantic.report_series_query import ReportSeriesQuery

class ReportQuery(BaseModel):
    # options, including format, scenarioId, projectHires
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='options')

    # series to evaluate
    series: typing.Optional[typing.List[ReportSeriesQuery]] = Field(None, alias='series')

    # filters to crosstab all results by (deprecated in reports V2, should use groupBy instead)
    filters: typing.Optional[typing.List[ReportFilter]] = Field(None, alias='filters')

    # content block to evaluate as a Carrot Template, as an alternative to using series
    content: typing.Optional[str] = Field(None, alias='content')

    # start date, in either relative (-7d) or exact (YYYY-MM-DD) format
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # end date, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    end_date: typing.Optional[str] = Field(None, alias='endDate')

    # interval, if the query is a timeseries; if no interval, query is crosstabbed
    interval: typing.Optional[Literal["DAY", "WEEK", "MONTH", "QUARTER", "FISCAL_QUARTER", "YEAR", "FISCAL_YEAR"]] = Field(None, alias='interval')

    interval_dates: typing.Optional[ReportQueryIntervalDates] = Field(None, alias='intervalDates')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
