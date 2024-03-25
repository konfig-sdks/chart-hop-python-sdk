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


class RequiredGroupParent(TypedDict):
    # globally unique id
    id: str

    # type of the parent
    type: str

class OptionalGroupParent(TypedDict, total=False):
    pass

class GroupParent(RequiredGroupParent, OptionalGroupParent):
    pass
