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

class CreateJobLevel(BaseModel):
    # human-readable name of job level
    label: str = Field(alias='label')

    # job level code
    code: typing.Optional[str] = Field(None, alias='code')

    benchmark_type: typing.Optional[EnumValue] = Field(None, alias='benchmarkType')

    benchmark_level: typing.Optional[EnumValue] = Field(None, alias='benchmarkLevel')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
