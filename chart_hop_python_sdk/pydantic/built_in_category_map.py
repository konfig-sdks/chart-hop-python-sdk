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

from chart_hop_python_sdk.pydantic.built_in_category_map_field_ids import BuiltInCategoryMapFieldIds

class BuiltInCategoryMap(BaseModel):
    # id of the built-in category
    category_id: str = Field(alias='categoryId')

    field_ids: BuiltInCategoryMapFieldIds = Field(alias='fieldIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
