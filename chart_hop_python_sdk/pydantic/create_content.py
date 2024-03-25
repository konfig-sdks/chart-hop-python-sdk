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

from chart_hop_python_sdk.pydantic.content_block import ContentBlock
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class CreateContent(BaseModel):
    # title of the content page
    title: str = Field(alias='title')

    # parent content id in the hierarchy
    parent_content_id: typing.Optional[str] = Field(None, alias='parentContentId')

    # full path to the content, if not set, defaults to an id/slug generated URL
    path: typing.Optional[str] = Field(None, alias='path')

    # content blocks
    blocks: typing.Optional[typing.List[ContentBlock]] = Field(None, alias='blocks')

    # path to the image for the page
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    # emoji, if an emoji is used to represent the page
    emoji: typing.Optional[str] = Field(None, alias='emoji')

    # path to the cover image for the content page
    cover_image_path: typing.Optional[str] = Field(None, alias='coverImagePath')

    # sensitivity level (ORG public, HIGHly sensitive, or PRIVATE)
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # list of users and groups who have the content shared with them
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # current status of the content page
    status: typing.Optional[Literal["DRAFT", "ACTIVE", "ARCHIVED"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
