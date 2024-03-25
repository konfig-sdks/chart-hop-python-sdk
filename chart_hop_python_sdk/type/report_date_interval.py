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


class RequiredReportDateInterval(TypedDict):
    startDate: date

    endDate: date

class OptionalReportDateInterval(TypedDict, total=False):
    partialStartDate: date

    partialEndDate: date

class ReportDateInterval(RequiredReportDateInterval, OptionalReportDateInterval):
    pass
