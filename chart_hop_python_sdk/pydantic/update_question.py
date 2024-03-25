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

class UpdateQuestion(BaseModel):
    # text of the question
    question: typing.Optional[str] = Field(None, alias='question')

    # if the question is linked to a field, the id of that field. Any question responses will be automatically saved to the field
    field_id: typing.Optional[str] = Field(None, alias='fieldId')

    # datatype of the question
    type: typing.Optional[Literal["ADDRESS", "BOOLEAN", "COMP", "COMPOUND", "COMP_BAND", "CONTACTS", "CURRENCY", "DATE", "DECIMAL", "ELAPSED_DAYS", "ELAPSED_MONTHS", "ELAPSED_YEARS", "EMAIL", "ENUM", "ENUM_EXPR", "ENUM_MULTI", "ENUM_SCALE", "EXPR", "FILE", "GROUP", "GROUPS", "GROUP_ASSIGNMENTS", "GROUP_TYPE", "IMAGE", "INTEGER", "JOB", "JOBS", "JOB_TIER", "LIST", "MONEY", "NAME", "OBJECT", "PAY_INTERVAL", "PERCENT", "PERSON", "PERSONS", "PHONE", "STOCKGRANT", "STRING", "TABLE_REF", "TEXT", "TIMEOFF", "TIMESTAMP", "TRACKED_GROUP", "URL", "USER", "VARIABLE_COMP", "VARIABLE_COMPS"]] = Field(None, alias='type')

    # plural type of the question datatype (either SINGLE, LIST, or SET)
    plural: typing.Optional[Literal["SINGLE", "LIST", "SET"]] = Field(None, alias='plural')

    # possible values (enum type only)
    values: typing.Optional[typing.List[EnumValue]] = Field(None, alias='values')

    # validation options
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
