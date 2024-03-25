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

from chart_hop_python_sdk.type.media_versions import MediaVersions

class RequiredMedia(TypedDict):
    # globally unique id of media
    id: str

    # path to the file in media S3 bucket
    path: str

    # mime type of file
    type: str

    versions: MediaVersions

    # created by user id
    createId: str

    # created timestamp
    createAt: str

class OptionalMedia(TypedDict, total=False):
    # parent org id, if the media belongs to an organization
    orgId: str

    # size of file in bytes
    bytes: int

    # width of image in pixels
    width: int

    # height of image in pixels
    height: int

class Media(RequiredMedia, OptionalMedia):
    pass
