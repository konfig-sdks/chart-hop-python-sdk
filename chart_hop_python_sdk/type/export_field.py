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


class RequiredExportField(TypedDict):
    # human-readable full name of field
    label: str

    # short field name
    name: str

    # entity type of field
    dataType: str

    # type of field
    appliesTo: str

    # dated
    dated: str

    # sensitivity
    sensitivity: str

    # category
    category: str

    # in use
    inUse: str

class OptionalExportField(TypedDict, total=False):
    pass

class ExportField(RequiredExportField, OptionalExportField):
    pass
