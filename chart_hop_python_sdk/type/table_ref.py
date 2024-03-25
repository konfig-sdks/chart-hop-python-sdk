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


class RequiredTableRef(TypedDict):
    # the table id this field references
    tableId: str

    # the table name this field references
    tableName: str

class OptionalTableRef(TypedDict, total=False):
    pass

class TableRef(RequiredTableRef, OptionalTableRef):
    pass
