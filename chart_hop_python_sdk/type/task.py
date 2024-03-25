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

class RequiredTask(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # user who is responsible for the task
    userId: str

    # type of task
    type: str

    # the primary entity being referenced by the task - for example for a FORM_SUBMIT, this will be the form
    entityId: str

    # status of this task
    status: str

class OptionalTask(TypedDict, total=False):
    # parent assessment id that this task belongs to
    assessmentId: str

    # parent entity id that this task belongs to, should be used with entityId
    parentEntityId: str

    # the optional target entity being referenced by the task - for example for a FORM_SUBMIT, this will be the person
    targetId: str

    # timestamp that the task was done, if it was done
    doneAt: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # The message attached to this task
    message: str

    # users who are specifically granted permission to view or edit this task
    shareAccess: typing.List[ShareAccess]

    # the optional path of this task (only applies to Type == ORG_IMPORT)
    path: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

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

class Task(RequiredTask, OptionalTask):
    pass
