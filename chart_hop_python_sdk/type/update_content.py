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

from chart_hop_python_sdk.type.content_block import ContentBlock
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredUpdateContent(TypedDict):
    pass

class OptionalUpdateContent(TypedDict, total=False):
    # title of the content page
    title: str

    # parent content id in the hierarchy
    parentContentId: str

    # full path to the content, if not set, defaults to an id/slug generated URL
    path: str

    # content blocks
    blocks: typing.List[ContentBlock]

    # path to the image for the page
    imagePath: str

    # emoji, if an emoji is used to represent the page
    emoji: str

    # path to the cover image for the content page
    coverImagePath: str

    # sensitivity level (ORG public, HIGHly sensitive, or PRIVATE)
    sensitive: str

    # list of users and groups who have the content shared with them
    shareAccess: typing.List[ShareAccess]

    # current status of the content page
    status: str

class UpdateContent(RequiredUpdateContent, OptionalUpdateContent):
    pass
