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

from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredUpdateTask(TypedDict):
    pass

class OptionalUpdateTask(TypedDict, total=False):
    # status of this task
    status: str

    # The message attached to this task
    message: str

    # users who are specifically granted permission to view or edit this task
    shareAccess: typing.List[ShareAccess]

    # id of the TaskConfig
    taskConfigId: str

    # slug used to reference tasks in events
    slug: str

    # due date for the task
    dueAt: str

    # what action to take when the task is past its due date
    pastDueAction: str

    # check for if the task can be skipped
    isSkippable: bool

class UpdateTask(RequiredUpdateTask, OptionalUpdateTask):
    pass
