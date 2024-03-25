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

from chart_hop_python_sdk.type.create_category_field_ids import CreateCategoryFieldIds
from chart_hop_python_sdk.type.create_category_native_fields import CreateCategoryNativeFields

class RequiredCreateCategory(TypedDict):
    # human-readable label of category
    label: str

class OptionalCreateCategory(TypedDict, total=False):
    # parent organization id (empty if built-in)
    orgId: str

    fieldIds: CreateCategoryFieldIds

    nativeFields: CreateCategoryNativeFields

class CreateCategory(RequiredCreateCategory, OptionalCreateCategory):
    pass
