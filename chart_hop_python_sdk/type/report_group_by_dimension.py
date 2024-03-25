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

from chart_hop_python_sdk.type.report_group_by_key import ReportGroupByKey

class RequiredReportGroupByDimension(TypedDict):
    # list of keys appearing in the groupBy
    keys: typing.List[ReportGroupByKey]

class OptionalReportGroupByDimension(TypedDict, total=False):
    pass

class ReportGroupByDimension(RequiredReportGroupByDimension, OptionalReportGroupByDimension):
    pass
