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

from chart_hop_python_sdk.type.action_step import ActionStep
from chart_hop_python_sdk.type.partial_action_tags import PartialActionTags

class RequiredPartialAction(TypedDict):
    pass

class OptionalPartialAction(TypedDict, total=False):
    tags: PartialActionTags

    # description of the action
    description: str

    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # event pattern to match on, such as change.create.*
    event: str

    # cron schedule to run on, in crontab format
    cronSchedule: str

    # only run when matching a particular filter
    filter: str

    # list of steps to run when matching the event, schedule, and filter
    steps: typing.List[ActionStep]

    # status of the action
    status: str

    # the user to run the action as - normally the same as the user who created the action
    runUserId: str

    # whether to run with access to sensitive events or not
    sensitive: bool

    # organizational category for HRIS-themed actions
    category: str

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

class PartialAction(RequiredPartialAction, OptionalPartialAction):
    pass
