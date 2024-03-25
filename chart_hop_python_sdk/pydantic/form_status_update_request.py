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

from chart_hop_python_sdk.pydantic.form_status_update_request_form_ids import FormStatusUpdateRequestFormIds

class FormStatusUpdateRequest(BaseModel):
    # New status to update
    update_status: Literal["ACTIVE", "INACTIVE", "ARCHIVED"] = Field(alias='updateStatus')

    form_ids: FormStatusUpdateRequestFormIds = Field(alias='formIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
