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


class RequiredFormField(TypedDict):
    # field id
    fieldId: str

    # human readable label for this field in this form
    label: str

    # whether field is required or not
    required: bool

    # whether label is long-format
    longLabel: bool

class OptionalFormField(TypedDict, total=False):
    pass

class FormField(RequiredFormField, OptionalFormField):
    pass
