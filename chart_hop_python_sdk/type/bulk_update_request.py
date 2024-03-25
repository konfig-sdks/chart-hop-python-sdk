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

from chart_hop_python_sdk.type.bulk_update_request_job_ids import BulkUpdateRequestJobIds
from chart_hop_python_sdk.type.job_update import JobUpdate

class RequiredBulkUpdateRequest(TypedDict):
    jobIds: BulkUpdateRequestJobIds

    update: JobUpdate

    # date of update
    date: date

class OptionalBulkUpdateRequest(TypedDict, total=False):
    # scenario id
    scenarioId: str

    # note for update
    note: str

class BulkUpdateRequest(RequiredBulkUpdateRequest, OptionalBulkUpdateRequest):
    pass
