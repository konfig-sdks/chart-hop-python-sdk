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

from chart_hop_python_sdk.type.enum_value import EnumValue

class RequiredJobLevel(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable name of job level
    label: str

class OptionalJobLevel(TypedDict, total=False):
    # job level code
    code: str

    benchmarkType: EnumValue

    benchmarkLevel: EnumValue

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class JobLevel(RequiredJobLevel, OptionalJobLevel):
    pass
