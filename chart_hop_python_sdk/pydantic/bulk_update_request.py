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

from chart_hop_python_sdk.pydantic.bulk_update_request_job_ids import BulkUpdateRequestJobIds
from chart_hop_python_sdk.pydantic.job_update import JobUpdate

class BulkUpdateRequest(BaseModel):
    job_ids: BulkUpdateRequestJobIds = Field(alias='jobIds')

    update: JobUpdate = Field(alias='update')

    # date of update
    date: date = Field(alias='date')

    # scenario id
    scenario_id: typing.Optional[str] = Field(None, alias='scenarioId')

    # note for update
    note: typing.Optional[str] = Field(None, alias='note')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
