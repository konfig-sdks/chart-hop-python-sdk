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

class Task(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # user who is responsible for the task
    user_id: str = Field(alias='userId')

    # type of task
    type: Literal["FORM_SUBMIT", "CHANGE_APPROVE", "TIMEOFF_APPROVE", "SCENARIO_CHANGES_APPROVE", "SCENARIO_CHANGES_CREATE", "ORG_IMPORT", "COMP_REVIEW_APPROVAL_SUBMIT", "SCENARIO_APPROVAL_SUBMIT", "APPROVAL_CHAIN_UPDATE_FALLBACK_APPROVER", "ACTION"] = Field(alias='type')

    # the primary entity being referenced by the task - for example for a FORM_SUBMIT, this will be the form
    entity_id: str = Field(alias='entityId')

    # status of this task
    status: Literal["PENDING", "DONE", "EXPIRED", "SKIPPED"] = Field(alias='status')

    # parent assessment id that this task belongs to
    assessment_id: typing.Optional[str] = Field(None, alias='assessmentId')

    # parent entity id that this task belongs to, should be used with entityId
    parent_entity_id: typing.Optional[str] = Field(None, alias='parentEntityId')

    # the optional target entity being referenced by the task - for example for a FORM_SUBMIT, this will be the person
    target_id: typing.Optional[str] = Field(None, alias='targetId')

    # timestamp that the task was done, if it was done
    done_at: typing.Optional[str] = Field(None, alias='doneAt')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # The message attached to this task
    message: typing.Optional[str] = Field(None, alias='message')

    # users who are specifically granted permission to view or edit this task
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # the optional path of this task (only applies to Type == ORG_IMPORT)
    path: typing.Optional[str] = Field(None, alias='path')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

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
