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


class RequiredBuiltInFieldConfig(TypedDict):
    # reserved codename for the native field
    name: str

    # hidden state of the native field (specific to org)
    hidden: bool

class OptionalBuiltInFieldConfig(TypedDict, total=False):
    # decimal places to round native Money fields
    places: int

class BuiltInFieldConfig(RequiredBuiltInFieldConfig, OptionalBuiltInFieldConfig):
    pass
