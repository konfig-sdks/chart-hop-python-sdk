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


class Message(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # type of message
    type: Literal["CHAT", "EMAIL", "WEB"] = Field(alias='type')

    # type of notification (SUCCESS, ERR, ANNOUNCEMENT etc.)
    notification_type: Literal["SUCCESS", "WARN", "ERROR", "COMMENT", "TASK_COMPLETED", "TASK_ASSIGNED", "REMINDER", "ANNOUNCEMENT", "PROCESS_ERROR", "PROCESS_DONE"] = Field(alias='notificationType')

    # user who receives the message
    user_id: str = Field(alias='userId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # message title
    title: typing.Optional[str] = Field(None, alias='title')

    # message content
    content: typing.Optional[str] = Field(None, alias='content')

    # link to message content (if applicable)
    message_url: typing.Optional[str] = Field(None, alias='messageUrl')

    # key of message if applicable (e.g. product-tour, import-complete-{id})
    key: typing.Optional[str] = Field(None, alias='key')

    # read timestamp
    read_at: typing.Optional[str] = Field(None, alias='readAt')

    # seen timestamp
    seen_at: typing.Optional[str] = Field(None, alias='seenAt')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
