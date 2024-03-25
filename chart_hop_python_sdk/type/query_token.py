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


class RequiredQueryToken(TypedDict):
    # globally unique id for query token
    id: str

    # globally unique random token string
    token: str

    # id of org
    orgId: str

    # id of user
    userId: str

    # query type
    type: str

    # query params
    params: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # created timestamp
    createAt: str

    # expire timestamp
    expireAt: str

class OptionalQueryToken(TypedDict, total=False):
    # query path (deprecated)
    path: str

    # total number of uses
    accessCount: int

    # last active timestamp
    activeAt: str

class QueryToken(RequiredQueryToken, OptionalQueryToken):
    pass
