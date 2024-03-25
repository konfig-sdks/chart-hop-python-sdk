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


class RequiredMoney(TypedDict):
    amount: typing.Union[int, float]

    currency: str

class OptionalMoney(TypedDict, total=False):
    places: typing.Union[int, float]

class Money(RequiredMoney, OptionalMoney):
    pass
