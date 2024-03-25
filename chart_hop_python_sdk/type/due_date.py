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


class RequiredDueDate(TypedDict):
    type: str

    # due day, in either relative (-7d) or exact (YYYY-MM-DD) format
    dueDay: str

    # due time, which is a LocalTime
    dueTime: str

class OptionalDueDate(TypedDict, total=False):
    pass

class DueDate(RequiredDueDate, OptionalDueDate):
    pass
