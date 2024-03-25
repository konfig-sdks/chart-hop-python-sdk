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

from chart_hop_python_sdk.type.block_fields import BlockFields

class RequiredBlock(TypedDict):
    pass

class OptionalBlock(TypedDict, total=False):
    # human readable label for this block
    label: str

    # filter condition expression applied to this block, used to determine whether the content appears on the target or not
    targetFilter: str

    # filter condition expression applied to this block, relative to the viewer
    readFilter: str

    fields: BlockFields

    # template content returned in this block
    content: str

class Block(RequiredBlock, OptionalBlock):
    pass
