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


class FormCollectRequest(BaseModel):
    # Is this a preview?
    preview: bool = Field(alias='preview')

    # the assessment id that this form collection request aligns to (for example a performance review cycle)
    assessment_id: typing.Optional[str] = Field(None, alias='assessmentId')

    # filter query to apply on who should receive the form collection request
    target_filter: typing.Optional[str] = Field(None, alias='targetFilter')

    # Filter to for jobs/person that match via relationship
    submit_filter: typing.Optional[str] = Field(None, alias='submitFilter')

    # message to include in notification
    message: typing.Optional[str] = Field(None, alias='message')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
