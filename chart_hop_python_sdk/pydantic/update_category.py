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

from chart_hop_python_sdk.pydantic.update_category_field_ids import UpdateCategoryFieldIds
from chart_hop_python_sdk.pydantic.update_category_native_fields import UpdateCategoryNativeFields

class UpdateCategory(BaseModel):
    # human-readable label of category
    label: typing.Optional[str] = Field(None, alias='label')

    field_ids: typing.Optional[UpdateCategoryFieldIds] = Field(None, alias='fieldIds')

    native_fields: typing.Optional[UpdateCategoryNativeFields] = Field(None, alias='nativeFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
