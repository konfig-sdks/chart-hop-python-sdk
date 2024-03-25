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


class RequiredFormBlock(TypedDict):
    # Type of Form Block
    type: str

class OptionalFormBlock(TypedDict, total=False):
    # unique id for the block
    id: str

    # field code name
    fieldName: str

    # Content of Content Block
    content: str

    # whether field is required or not
    required: bool

    # question id, for questions
    questionId: str

class FormBlock(RequiredFormBlock, OptionalFormBlock):
    pass
