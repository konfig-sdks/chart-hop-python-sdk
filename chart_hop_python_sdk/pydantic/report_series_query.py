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

from chart_hop_python_sdk.pydantic.group_by_config import GroupByConfig

class ReportSeriesQuery(BaseModel):
    # label to use
    label: str = Field(alias='label')

    # color to use
    color: str = Field(alias='color')

    # y-value to calculate
    y: str = Field(alias='y')

    # special options, such as scenarioId, format, projectHires
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='options')

    # x-value to calculate (only needed for future scatterplot feature)
    x: typing.Optional[str] = Field(None, alias='x')

    # Configuration for aggregations performed by the groupBy operator
    group_by_configs: typing.Optional[typing.List[GroupByConfig]] = Field(None, alias='groupByConfigs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
