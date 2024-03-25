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

from chart_hop_python_sdk.type.task import Task

class RequiredTaskFormSummary(TypedDict):
    # Number of FORM_SUBMIT tasks that are marked as DONE
    submitCount: int

    # Number CHANGE_APPROVE tasks that are done.
    approveCount: int

    # Number FORM_SUBMIT tasks that are PENDING
    pendingCount: int

    # Number FORM_SUBMIT tasks that are SKIPPED
    skippedCount: int

    # Number FORM_SUBMIT tasks that are EXPIRED
    expiredCount: int

    # Number of unique people included in the form
    peopleIncludedCount: int

    # List of Dto Tasks
    taskList: typing.List[Task]

class OptionalTaskFormSummary(TypedDict, total=False):
    pass

class TaskFormSummary(RequiredTaskFormSummary, OptionalTaskFormSummary):
    pass
