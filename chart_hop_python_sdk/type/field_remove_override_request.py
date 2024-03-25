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

from chart_hop_python_sdk.type.field_remove_override_request_field_ids import FieldRemoveOverrideRequestFieldIds

class RequiredFieldRemoveOverrideRequest(TypedDict):
    fieldIds: FieldRemoveOverrideRequestFieldIds

class OptionalFieldRemoveOverrideRequest(TypedDict, total=False):
    pass

class FieldRemoveOverrideRequest(RequiredFieldRemoveOverrideRequest, OptionalFieldRemoveOverrideRequest):
    pass
