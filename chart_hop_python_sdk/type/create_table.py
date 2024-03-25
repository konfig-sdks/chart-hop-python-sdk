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

from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredCreateTable(TypedDict):
    # name of table
    name: str

    # whether or not the table is time tracked with effective dates (allows time travel or not). If false, then the values set in the table will be the same across all dates.
    effectiveDated: bool

class OptionalCreateTable(TypedDict, total=False):
    # human readable label for the table
    label: str

    # base sensitivity of this table and entities in it -- should be either ORG or HIGH
    sensitive: str

    # users who are specifically granted permission to this table
    shareAccess: typing.List[ShareAccess]

class CreateTable(RequiredCreateTable, OptionalCreateTable):
    pass
