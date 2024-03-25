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


class RequiredMessage(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # type of message
    type: str

    # type of notification (SUCCESS, ERR, ANNOUNCEMENT etc.)
    notificationType: str

    # user who receives the message
    userId: str

    # created timestamp
    createAt: str

class OptionalMessage(TypedDict, total=False):
    # message title
    title: str

    # message content
    content: str

    # link to message content (if applicable)
    messageUrl: str

    # key of message if applicable (e.g. product-tour, import-complete-{id})
    key: str

    # read timestamp
    readAt: str

    # seen timestamp
    seenAt: str

    # created by user id
    createId: str

class Message(RequiredMessage, OptionalMessage):
    pass
