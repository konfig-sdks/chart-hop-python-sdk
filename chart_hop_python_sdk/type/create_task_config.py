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

from chart_hop_python_sdk.type.due_date import DueDate

class RequiredCreateTaskConfig(TypedDict):
    # the primary entity being referenced by the task config
    entityId: str

    # type of task generated by the task config
    type: str

    # sets pastDueAction on the task when it's generated
    pastDueAction: str

class OptionalCreateTaskConfig(TypedDict, total=False):
    # description for all tasks associated with the config that should be used in notifications
    description: str

    # parent assessment id that this task config belongs to
    assessmentId: str

    # parent entity id that this task config belongs to, should be used with entityId
    parentEntityId: str

    dueDate: DueDate

    # sets isSkippable on the task
    isSkippable: bool

    # human-readable label that should be used for all tasks associated with the config as the task name
    label: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class CreateTaskConfig(RequiredCreateTaskConfig, OptionalCreateTaskConfig):
    pass
