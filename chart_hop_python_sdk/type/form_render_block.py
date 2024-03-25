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

from chart_hop_python_sdk.type.enum_value import EnumValue
from chart_hop_python_sdk.type.form_render_block_options import FormRenderBlockOptions

class RequiredFormRenderBlock(TypedDict):
    type: str

    id: str

class OptionalFormRenderBlock(TypedDict, total=False):
    name: str

    question: str

    dataType: str

    plural: str

    values: typing.List[EnumValue]

    options: FormRenderBlockOptions

    value: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    required: bool

    content: str

    label: str

class FormRenderBlock(RequiredFormRenderBlock, OptionalFormRenderBlock):
    pass
