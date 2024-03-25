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


class RequiredGroupType(TypedDict):
    # globally unique id
    id: str

    # unique name of group
    name: str

    # unique slug of group
    slug: str

class OptionalGroupType(TypedDict, total=False):
    # parent organization id
    orgId: str

    # whether the group requires members to be positions
    requirePositions: bool

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

class GroupType(RequiredGroupType, OptionalGroupType):
    pass
