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

from chart_hop_python_sdk.pydantic.template_tags import TemplateTags

class Template(BaseModel):
    tags: TemplateTags = Field(alias='tags')

    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # template name, must be unique to organization
    name: str = Field(alias='name')

    # template content
    content: str = Field(alias='content')

    # template content format - must be MARKDOWN
    format: Literal["HTML", "MARKDOWN", "TEXT"] = Field(alias='format')

    # type of template
    type: Literal["DOCUMENT", "EMAIL"] = Field(alias='type')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # last updated by user id
    update_id: str = Field(alias='updateId')

    # last updated timestamp
    update_at: str = Field(alias='updateAt')

    # description of template
    description: typing.Optional[str] = Field(None, alias='description')

    # template inline stylesheet
    stylesheet: typing.Optional[str] = Field(None, alias='stylesheet')

    # document filename CQL
    filename: typing.Optional[str] = Field(None, alias='filename')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
