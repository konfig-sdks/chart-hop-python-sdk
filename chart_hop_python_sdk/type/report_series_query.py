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

from chart_hop_python_sdk.type.group_by_config import GroupByConfig

class RequiredReportSeriesQuery(TypedDict):
    # label to use
    label: str

    # color to use
    color: str

    # y-value to calculate
    y: str

    # special options, such as scenarioId, format, projectHires
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalReportSeriesQuery(TypedDict, total=False):
    # x-value to calculate (only needed for future scatterplot feature)
    x: str

    # Configuration for aggregations performed by the groupBy operator
    groupByConfigs: typing.List[GroupByConfig]

class ReportSeriesQuery(RequiredReportSeriesQuery, OptionalReportSeriesQuery):
    pass
