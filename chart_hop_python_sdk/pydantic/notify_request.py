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


class NotifyRequest(BaseModel):
    # email subject line
    email_subject: typing.Optional[str] = Field(None, alias='emailSubject')

    # email HTML content
    email_content_html: typing.Optional[str] = Field(None, alias='emailContentHtml')

    # email Markdown content
    email_markdown: typing.Optional[str] = Field(None, alias='emailMarkdown')

    # chat Markdown content, if chat message should be different/abbreviated
    chat_markdown: typing.Optional[str] = Field(None, alias='chatMarkdown')

    # Type of notification
    notify_type: typing.Optional[str] = Field(None, alias='notifyType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
