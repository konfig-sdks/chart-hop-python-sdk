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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.task import Task

class TaskFormSummary(BaseModel):
    # Number of FORM_SUBMIT tasks that are marked as DONE
    submit_count: int = Field(alias='submitCount')

    # Number CHANGE_APPROVE tasks that are done.
    approve_count: int = Field(alias='approveCount')

    # Number FORM_SUBMIT tasks that are PENDING
    pending_count: int = Field(alias='pendingCount')

    # Number FORM_SUBMIT tasks that are SKIPPED
    skipped_count: int = Field(alias='skippedCount')

    # Number FORM_SUBMIT tasks that are EXPIRED
    expired_count: int = Field(alias='expiredCount')

    # Number of unique people included in the form
    people_included_count: int = Field(alias='peopleIncludedCount')

    # List of Dto Tasks
    task_list: typing.List[Task] = Field(alias='taskList')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
