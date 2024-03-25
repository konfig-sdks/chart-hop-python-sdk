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


class RequiredGroupGraphCount(TypedDict):
    # number of jobs
    jobCount: typing.Union[int, float]

    # number of persons
    personCount: typing.Union[int, float]

    # number of groups
    groupCount: typing.Union[int, float]

class OptionalGroupGraphCount(TypedDict, total=False):
    pass

class GroupGraphCount(RequiredGroupGraphCount, OptionalGroupGraphCount):
    pass
