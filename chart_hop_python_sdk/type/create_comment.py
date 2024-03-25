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

from chart_hop_python_sdk.type.markup import Markup

class RequiredCreateComment(TypedDict):
    # entity the comment was posted on
    entityId: str

    # type of entity the comment was posted on
    entityType: str

    content: Markup

class OptionalCreateComment(TypedDict, total=False):
    # parent entity id that this comment belongs to, should be used with entityId
    parentEntityId: str

class CreateComment(RequiredCreateComment, OptionalCreateComment):
    pass
