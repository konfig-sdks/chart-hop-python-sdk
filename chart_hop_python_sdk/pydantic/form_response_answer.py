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


class FormResponseAnswer(BaseModel):
    id: str = Field(alias='id')

    question_id: str = Field(alias='questionId')

    value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='value')

    type: typing.Optional[Literal["ADDRESS", "BOOLEAN", "COMP", "COMPOUND", "COMP_BAND", "CONTACTS", "CURRENCY", "DATE", "DECIMAL", "ELAPSED_DAYS", "ELAPSED_MONTHS", "ELAPSED_YEARS", "EMAIL", "ENUM", "ENUM_EXPR", "ENUM_MULTI", "ENUM_SCALE", "EXPR", "FILE", "GROUP", "GROUPS", "GROUP_ASSIGNMENTS", "GROUP_TYPE", "IMAGE", "INTEGER", "JOB", "JOBS", "JOB_TIER", "LIST", "MONEY", "NAME", "OBJECT", "PAY_INTERVAL", "PERCENT", "PERSON", "PERSONS", "PHONE", "STOCKGRANT", "STRING", "TABLE_REF", "TEXT", "TIMEOFF", "TIMESTAMP", "TRACKED_GROUP", "URL", "USER", "VARIABLE_COMP", "VARIABLE_COMPS"]] = Field(None, alias='type')

    plural: typing.Optional[Literal["SINGLE", "LIST", "SET"]] = Field(None, alias='plural')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
