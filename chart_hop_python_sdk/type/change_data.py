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

from chart_hop_python_sdk.type.change import Change
from chart_hop_python_sdk.type.change_data_data import ChangeDataData
from chart_hop_python_sdk.type.change_data_locked_fields import ChangeDataLockedFields

class RequiredChangeData(TypedDict):
    change: Change

    data: ChangeDataData

    # the annualized impact of this change, denoted in organization's currency
    cost: typing.Union[int, float]

class OptionalChangeData(TypedDict, total=False):
    lockedFields: ChangeDataLockedFields

class ChangeData(RequiredChangeData, OptionalChangeData):
    pass
