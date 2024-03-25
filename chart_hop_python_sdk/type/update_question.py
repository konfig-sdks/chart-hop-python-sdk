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

class RequiredUpdateQuestion(TypedDict):
    pass

class OptionalUpdateQuestion(TypedDict, total=False):
    # text of the question
    question: str

    # if the question is linked to a field, the id of that field. Any question responses will be automatically saved to the field
    fieldId: str

    # datatype of the question
    type: str

    # plural type of the question datatype (either SINGLE, LIST, or SET)
    plural: str

    # possible values (enum type only)
    values: typing.List[EnumValue]

    # validation options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class UpdateQuestion(RequiredUpdateQuestion, OptionalUpdateQuestion):
    pass
