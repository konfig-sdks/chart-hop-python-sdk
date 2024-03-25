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

from chart_hop_python_sdk.type.form_submit_request_blocks_data import FormSubmitRequestBlocksData
from chart_hop_python_sdk.type.form_submit_request_data import FormSubmitRequestData

class RequiredFormSubmitRequest(TypedDict):
    # person data is being filled out on behalf of
    personId: str

    data: FormSubmitRequestData

class OptionalFormSubmitRequest(TypedDict, total=False):
    blocksData: FormSubmitRequestBlocksData

class FormSubmitRequest(RequiredFormSubmitRequest, OptionalFormSubmitRequest):
    pass
