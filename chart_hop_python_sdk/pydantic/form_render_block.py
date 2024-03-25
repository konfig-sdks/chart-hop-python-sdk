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

from chart_hop_python_sdk.pydantic.enum_value import EnumValue
from chart_hop_python_sdk.pydantic.form_render_block_options import FormRenderBlockOptions

class FormRenderBlock(BaseModel):
    type: Literal["QUESTION", "CONTENT"] = Field(alias='type')

    id: str = Field(alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    question: typing.Optional[str] = Field(None, alias='question')

    data_type: typing.Optional[Literal["ADDRESS", "BOOLEAN", "COMP", "COMPOUND", "COMP_BAND", "CONTACTS", "CURRENCY", "DATE", "DECIMAL", "ELAPSED_DAYS", "ELAPSED_MONTHS", "ELAPSED_YEARS", "EMAIL", "ENUM", "ENUM_EXPR", "ENUM_MULTI", "ENUM_SCALE", "EXPR", "FILE", "GROUP", "GROUPS", "GROUP_ASSIGNMENTS", "GROUP_TYPE", "IMAGE", "INTEGER", "JOB", "JOBS", "JOB_TIER", "LIST", "MONEY", "NAME", "OBJECT", "PAY_INTERVAL", "PERCENT", "PERSON", "PERSONS", "PHONE", "STOCKGRANT", "STRING", "TABLE_REF", "TEXT", "TIMEOFF", "TIMESTAMP", "TRACKED_GROUP", "URL", "USER", "VARIABLE_COMP", "VARIABLE_COMPS"]] = Field(None, alias='dataType')

    plural: typing.Optional[Literal["SINGLE", "LIST", "SET"]] = Field(None, alias='plural')

    values: typing.Optional[typing.List[EnumValue]] = Field(None, alias='values')

    options: typing.Optional[FormRenderBlockOptions] = Field(None, alias='options')

    value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='value')

    required: typing.Optional[bool] = Field(None, alias='required')

    content: typing.Optional[str] = Field(None, alias='content')

    label: typing.Optional[str] = Field(None, alias='label')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
