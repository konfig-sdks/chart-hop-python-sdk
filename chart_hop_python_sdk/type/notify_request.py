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


class RequiredNotifyRequest(TypedDict):
    pass

class OptionalNotifyRequest(TypedDict, total=False):
    # email subject line
    emailSubject: str

    # email HTML content
    emailContentHtml: str

    # email Markdown content
    emailMarkdown: str

    # chat Markdown content, if chat message should be different/abbreviated
    chatMarkdown: str

    # Type of notification
    notifyType: str

class NotifyRequest(RequiredNotifyRequest, OptionalNotifyRequest):
    pass
