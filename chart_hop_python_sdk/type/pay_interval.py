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

from chart_hop_python_sdk.type.money import Money

class RequiredPayInterval(TypedDict):
    # Interval (annual or hourly)
    interval: str

    pay: Money

class OptionalPayInterval(TypedDict, total=False):
    # working hours per week if interval=hourly
    hoursPerWeek: int

    # working weeks per year if interval=hourly
    weeksPerYear: int

class PayInterval(RequiredPayInterval, OptionalPayInterval):
    pass
