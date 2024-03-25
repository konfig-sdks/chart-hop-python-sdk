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

from chart_hop_python_sdk.type.create_category_sort_category_ids import CreateCategorySortCategoryIds

class RequiredCreateCategorySort(TypedDict):
    # parent organization id (empty if built-in)
    orgId: str

    categoryIds: CreateCategorySortCategoryIds

class OptionalCreateCategorySort(TypedDict, total=False):
    pass

class CreateCategorySort(RequiredCreateCategorySort, OptionalCreateCategorySort):
    pass
