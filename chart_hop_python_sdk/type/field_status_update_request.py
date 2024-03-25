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

from chart_hop_python_sdk.type.field_status_update_request_field_ids import FieldStatusUpdateRequestFieldIds
from chart_hop_python_sdk.type.field_status_update_request_reserved_field_names import FieldStatusUpdateRequestReservedFieldNames

class RequiredFieldStatusUpdateRequest(TypedDict):
    # New status to update
    updateStatus: str

    fieldIds: FieldStatusUpdateRequestFieldIds

    reservedFieldNames: FieldStatusUpdateRequestReservedFieldNames

class OptionalFieldStatusUpdateRequest(TypedDict, total=False):
    pass

class FieldStatusUpdateRequest(RequiredFieldStatusUpdateRequest, OptionalFieldStatusUpdateRequest):
    pass
