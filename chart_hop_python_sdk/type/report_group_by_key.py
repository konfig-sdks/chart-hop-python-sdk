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


class RequiredReportGroupByKey(TypedDict):
    # unique string identifier for this key
    id: str

    # color for this key, prior to any overrides
    color: str

    # label for this key, prior to any overrides
    label: str

class OptionalReportGroupByKey(TypedDict, total=False):
    pass

class ReportGroupByKey(RequiredReportGroupByKey, OptionalReportGroupByKey):
    pass
