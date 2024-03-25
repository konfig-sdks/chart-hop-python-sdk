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


class RequiredGrantAlias(TypedDict):
    grantType: str

    enabled: bool

class OptionalGrantAlias(TypedDict, total=False):
    alias: str

class GrantAlias(RequiredGrantAlias, OptionalGrantAlias):
    pass
