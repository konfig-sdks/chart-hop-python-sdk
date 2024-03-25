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


class RequiredLabelOverride(TypedDict):
    # The unique identifier to use to locate the key to override. For entities and enum values, this will be an id. For numbers, this will be the normalized numeric representation. For others, this will be the string
    id: str

class OptionalLabelOverride(TypedDict, total=False):
    # If set, overrides this label
    label: str

    # If set, overrides the default color
    color: str

    # If set, overrides the sorting order
    sort: int

class LabelOverride(RequiredLabelOverride, OptionalLabelOverride):
    pass
