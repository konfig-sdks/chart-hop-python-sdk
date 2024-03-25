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


class RequiredMultiplier(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable name of multiplier
    label: str

    # amount to multiply the initial value by
    value: typing.Union[int, float]

    # calculated expression to match against the job
    expr: str

class OptionalMultiplier(TypedDict, total=False):
    code: str

    # tag to group multipliers together by
    category: str

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

class Multiplier(RequiredMultiplier, OptionalMultiplier):
    pass
