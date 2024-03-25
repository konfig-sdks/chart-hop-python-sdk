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


class FormBlock(BaseModel):
    # Type of Form Block
    type: Literal["QUESTION", "CONTENT"] = Field(alias='type')

    # unique id for the block
    id: typing.Optional[str] = Field(None, alias='id')

    # field code name
    field_name: typing.Optional[str] = Field(None, alias='fieldName')

    # Content of Content Block
    content: typing.Optional[str] = Field(None, alias='content')

    # whether field is required or not
    required: typing.Optional[bool] = Field(None, alias='required')

    # question id, for questions
    question_id: typing.Optional[str] = Field(None, alias='questionId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
