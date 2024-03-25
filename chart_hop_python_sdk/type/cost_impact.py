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

from chart_hop_python_sdk.type.cost_impact_months import CostImpactMonths

class RequiredCostImpact(TypedDict):
    # total annual run-rate impact
    annual: typing.Union[int, float]

    # first month to be affected
    firstMonth: str

    months: CostImpactMonths

class OptionalCostImpact(TypedDict, total=False):
    pass

class CostImpact(RequiredCostImpact, OptionalCostImpact):
    pass
