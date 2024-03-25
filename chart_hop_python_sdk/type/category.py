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

from chart_hop_python_sdk.type.category_field_ids import CategoryFieldIds
from chart_hop_python_sdk.type.category_native_fields import CategoryNativeFields

class RequiredCategory(TypedDict):
    # globally unique id
    id: str

    # human-readable label of category
    label: str

class OptionalCategory(TypedDict, total=False):
    # parent organization id (empty if built-in)
    orgId: str

    fieldIds: CategoryFieldIds

    nativeFields: CategoryNativeFields

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class Category(RequiredCategory, OptionalCategory):
    pass
