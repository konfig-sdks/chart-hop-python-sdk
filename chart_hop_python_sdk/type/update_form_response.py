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

from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredUpdateFormResponse(TypedDict):
    pass

class OptionalUpdateFormResponse(TypedDict, total=False):
    # list of share access, if the form response has been shared with anyone
    shareAccess: typing.List[ShareAccess]

class UpdateFormResponse(RequiredUpdateFormResponse, OptionalUpdateFormResponse):
    pass
