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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.field_status_update_request_field_ids import FieldStatusUpdateRequestFieldIds
from chart_hop_python_sdk.pydantic.field_status_update_request_reserved_field_names import FieldStatusUpdateRequestReservedFieldNames

class FieldStatusUpdateRequest(BaseModel):
    # New status to update
    update_status: Literal["ACTIVE", "HIDDEN"] = Field(alias='updateStatus')

    field_ids: FieldStatusUpdateRequestFieldIds = Field(alias='fieldIds')

    reserved_field_names: FieldStatusUpdateRequestReservedFieldNames = Field(alias='reservedFieldNames')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
