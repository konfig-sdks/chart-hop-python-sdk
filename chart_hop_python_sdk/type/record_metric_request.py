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


class RequiredRecordMetricRequest(TypedDict):
    # the name of the metric, for example kpi.revenue.arr
    metric: str

    # the numeric value of the metric
    value: typing.Union[int, float]

class OptionalRecordMetricRequest(TypedDict, total=False):
    # the date that the metric applies to (if blank, will default to today)
    date: date

class RecordMetricRequest(RequiredRecordMetricRequest, OptionalRecordMetricRequest):
    pass
