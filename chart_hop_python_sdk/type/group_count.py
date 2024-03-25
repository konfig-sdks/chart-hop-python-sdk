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


class RequiredGroupCount(TypedDict):
    # total number of groups
    totalGroupCount: typing.Union[int, float]

    # number of groups that are part of a larger group tree
    relationshipGroupCount: typing.Union[int, float]

    # number of orphaned groups that do not belong to any group tree
    orphanedGroupCount: typing.Union[int, float]

class OptionalGroupCount(TypedDict, total=False):
    pass

class GroupCount(RequiredGroupCount, OptionalGroupCount):
    pass
