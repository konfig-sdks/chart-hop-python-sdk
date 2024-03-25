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


class RequiredViewAsRequest(TypedDict):
    # org id
    orgId: str

    # scope being requested
    scope: str

class OptionalViewAsRequest(TypedDict, total=False):
    # person id
    personId: str

    # user id
    userId: str

    # role id
    roleId: str

class ViewAsRequest(RequiredViewAsRequest, OptionalViewAsRequest):
    pass
