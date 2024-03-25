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

from chart_hop_python_sdk.type.outbound_value_mapper import OutboundValueMapper

class RequiredOutboundFieldMapper(TypedDict):
    description: str

    namespace: str

    valueMappers: typing.List[OutboundValueMapper]

class OptionalOutboundFieldMapper(TypedDict, total=False):
    id: str

    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OutboundFieldMapper(RequiredOutboundFieldMapper, OptionalOutboundFieldMapper):
    pass
