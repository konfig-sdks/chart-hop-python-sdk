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

from chart_hop_python_sdk.pydantic.category_field_ids import CategoryFieldIds
from chart_hop_python_sdk.pydantic.category_native_fields import CategoryNativeFields

class Category(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # human-readable label of category
    label: str = Field(alias='label')

    # parent organization id (empty if built-in)
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    field_ids: typing.Optional[CategoryFieldIds] = Field(None, alias='fieldIds')

    native_fields: typing.Optional[CategoryNativeFields] = Field(None, alias='nativeFields')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
