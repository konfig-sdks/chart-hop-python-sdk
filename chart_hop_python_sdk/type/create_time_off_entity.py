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


class RequiredCreateTimeOffEntity(TypedDict):
    # person taking the time off
    personId: str

    # start date of time off, inclusive
    startDate: date

    # end date of time off, inclusive
    endDate: date

class OptionalCreateTimeOffEntity(TypedDict, total=False):
    # external identifier, if time off synced from external system
    externalId: str

    # number of days used
    days: typing.Union[int, float]

    # number of hours used
    hours: typing.Union[int, float]

    # type of time off
    typeDescription: str

    # notes on the time off
    note: str

    # approval status of the time off
    approval: str

class CreateTimeOffEntity(RequiredCreateTimeOffEntity, OptionalCreateTimeOffEntity):
    pass
