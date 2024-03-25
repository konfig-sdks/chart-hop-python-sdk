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

from chart_hop_python_sdk.type.update_category_sort_category_ids import UpdateCategorySortCategoryIds

class RequiredUpdateCategorySort(TypedDict):
    pass

class OptionalUpdateCategorySort(TypedDict, total=False):
    categoryIds: UpdateCategorySortCategoryIds

class UpdateCategorySort(RequiredUpdateCategorySort, OptionalUpdateCategorySort):
    pass
