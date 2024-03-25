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

from chart_hop_python_sdk.type.access_action_fields import AccessActionFields
from chart_hop_python_sdk.type.access_action_types import AccessActionTypes

class RequiredAccessAction(TypedDict):
    action: str

class OptionalAccessAction(TypedDict, total=False):
    fields: AccessActionFields

    types: AccessActionTypes

class AccessAction(RequiredAccessAction, OptionalAccessAction):
    pass
