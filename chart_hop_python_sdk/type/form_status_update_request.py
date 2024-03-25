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

from chart_hop_python_sdk.type.form_status_update_request_form_ids import FormStatusUpdateRequestFormIds

class RequiredFormStatusUpdateRequest(TypedDict):
    # New status to update
    updateStatus: str

    formIds: FormStatusUpdateRequestFormIds

class OptionalFormStatusUpdateRequest(TypedDict, total=False):
    pass

class FormStatusUpdateRequest(RequiredFormStatusUpdateRequest, OptionalFormStatusUpdateRequest):
    pass
