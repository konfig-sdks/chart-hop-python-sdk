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

from chart_hop_python_sdk.type.update_operation import UpdateOperation

class RequiredBulkJobUpdateRequest(TypedDict):
    # list of update operations to perform
    updates: typing.List[UpdateOperation]

    # date of update
    date: date

class OptionalBulkJobUpdateRequest(TypedDict, total=False):
    # scenario id
    scenarioId: str

    # note for update
    note: str

class BulkJobUpdateRequest(RequiredBulkJobUpdateRequest, OptionalBulkJobUpdateRequest):
    pass
