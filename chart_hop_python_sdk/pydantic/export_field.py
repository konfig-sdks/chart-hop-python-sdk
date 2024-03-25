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


class ExportField(BaseModel):
    # human-readable full name of field
    label: str = Field(alias='label')

    # short field name
    name: str = Field(alias='name')

    # entity type of field
    data_type: str = Field(alias='dataType')

    # type of field
    applies_to: str = Field(alias='appliesTo')

    # dated
    dated: str = Field(alias='dated')

    # sensitivity
    sensitivity: str = Field(alias='sensitivity')

    # category
    category: str = Field(alias='category')

    # in use
    in_use: str = Field(alias='inUse')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
