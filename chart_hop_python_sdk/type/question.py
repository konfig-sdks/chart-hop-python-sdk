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

class RequiredQuestion(TypedDict):
    # globally unique id
    id: str

    # text of the question
    question: str

    # datatype of the question
    type: str

class OptionalQuestion(TypedDict, total=False):
    # parent organization id (empty if global)
    orgId: str

    # if the question is linked to a field, the id of that field. Any question responses will be automatically saved to the field
    fieldId: str

    # plural type of the question datatype (either SINGLE, LIST, or SET)
    plural: str

    # possible values (enum type only)
    values: typing.List[EnumValue]

    # validation options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class Question(RequiredQuestion, OptionalQuestion):
    pass
