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

from chart_hop_python_sdk.pydantic.media_versions import MediaVersions

class Media(BaseModel):
    # globally unique id of media
    id: str = Field(alias='id')

    # path to the file in media S3 bucket
    path: str = Field(alias='path')

    # mime type of file
    type: str = Field(alias='type')

    versions: MediaVersions = Field(alias='versions')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # parent org id, if the media belongs to an organization
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # size of file in bytes
    bytes: typing.Optional[int] = Field(None, alias='bytes')

    # width of image in pixels
    width: typing.Optional[int] = Field(None, alias='width')

    # height of image in pixels
    height: typing.Optional[int] = Field(None, alias='height')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
