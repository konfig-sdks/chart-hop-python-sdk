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

from chart_hop_python_sdk.type.money_range import MoneyRange
from chart_hop_python_sdk.type.value_range import ValueRange

class RequiredBasisCondition(TypedDict):
    conditionExpr: str

class OptionalBasisCondition(TypedDict, total=False):
    amountRange: MoneyRange

    valueRange: ValueRange

class BasisCondition(RequiredBasisCondition, OptionalBasisCondition):
    pass
