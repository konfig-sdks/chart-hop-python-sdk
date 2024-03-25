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

from chart_hop_python_sdk.pydantic.form_submit_request_blocks_data import FormSubmitRequestBlocksData
from chart_hop_python_sdk.pydantic.form_submit_request_data import FormSubmitRequestData

class FormSubmitRequest(BaseModel):
    # person data is being filled out on behalf of
    person_id: str = Field(alias='personId')

    data: FormSubmitRequestData = Field(alias='data')

    blocks_data: typing.Optional[FormSubmitRequestBlocksData] = Field(None, alias='blocksData')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
