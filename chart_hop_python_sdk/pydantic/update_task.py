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

from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class UpdateTask(BaseModel):
    # status of this task
    status: typing.Optional[Literal["PENDING", "DONE", "EXPIRED", "SKIPPED"]] = Field(None, alias='status')

    # The message attached to this task
    message: typing.Optional[str] = Field(None, alias='message')

    # users who are specifically granted permission to view or edit this task
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # id of the TaskConfig
    task_config_id: typing.Optional[str] = Field(None, alias='taskConfigId')

    # slug used to reference tasks in events
    slug: typing.Optional[str] = Field(None, alias='slug')

    # due date for the task
    due_at: typing.Optional[str] = Field(None, alias='dueAt')

    # what action to take when the task is past its due date
    past_due_action: typing.Optional[Literal["NONE", "SET_EXPIRED"]] = Field(None, alias='pastDueAction')

    # check for if the task can be skipped
    is_skippable: typing.Optional[bool] = Field(None, alias='isSkippable')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
