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


class RequiredOutboundValueMapper(TypedDict):
    charthopSide: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    externalSide: str

class OptionalOutboundValueMapper(TypedDict, total=False):
    id: str

    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OutboundValueMapper(RequiredOutboundValueMapper, OptionalOutboundValueMapper):
    pass
