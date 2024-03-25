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


class RequiredTimeOffEntity(TypedDict):
    # globally unique id of time off
    id: str

    # org that the time off belongs to
    orgId: str

    # person taking the time off
    personId: str

    # start date of time off, inclusive
    startDate: date

    # end date of time off, inclusive
    endDate: date

class OptionalTimeOffEntity(TypedDict, total=False):
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

    # timestamp of approval
    approvalAt: str

    # user who either is the next one requesting approval, or the user who did the final approval or rejection
    approvalUserId: str

    # requested at timestamp -- often the same as createAt
    requestAt: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # updated timestamp
    updateAt: str

    # updated by user id
    updateId: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class TimeOffEntity(RequiredTimeOffEntity, OptionalTimeOffEntity):
    pass
