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

from chart_hop_python_sdk.type.pay_interval import PayInterval
from chart_hop_python_sdk.type.variable_comp import VariableComp

class RequiredComp(TypedDict):
    pass

class OptionalComp(TypedDict, total=False):
    baseComp: PayInterval

    # variable compensation (money or percent)
    variableTargets: typing.List[VariableComp]

    # planned stock grant, in shares
    grantShares: int

    # planned stock grant, in value (based on the stock's currency, not the comp)
    grantValue: int

    # planned stock grant type
    grantType: str

class Comp(RequiredComp, OptionalComp):
    pass
