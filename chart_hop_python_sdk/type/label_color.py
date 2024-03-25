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


class RequiredLabelColor(TypedDict):
    # human-readable label for the value
    label: str

    # suggested color for the value
    color: str

class OptionalLabelColor(TypedDict, total=False):
    pass

class LabelColor(RequiredLabelColor, OptionalLabelColor):
    pass
