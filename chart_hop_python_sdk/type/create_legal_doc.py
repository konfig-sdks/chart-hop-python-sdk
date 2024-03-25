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


class RequiredCreateLegalDoc(TypedDict):
    # human-readable full name of form
    name: str

    # legal doc content
    content: str

    # content by date
    date: date

class OptionalCreateLegalDoc(TypedDict, total=False):
    pass

class CreateLegalDoc(RequiredCreateLegalDoc, OptionalCreateLegalDoc):
    pass