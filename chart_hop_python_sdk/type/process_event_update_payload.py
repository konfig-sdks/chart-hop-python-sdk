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


class RequiredProcessEventUpdatePayload(TypedDict):
    pass

class OptionalProcessEventUpdatePayload(TypedDict, total=False):
    key: str

    value: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    currency: str

    contactFormat: str

    errorMessage: str

class ProcessEventUpdatePayload(RequiredProcessEventUpdatePayload, OptionalProcessEventUpdatePayload):
    pass