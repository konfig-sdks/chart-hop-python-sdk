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

from chart_hop_python_sdk.pydantic.create_template_tags import CreateTemplateTags

class CreateTemplate(BaseModel):
    # template name, must be unique to organization
    name: str = Field(alias='name')

    # template content
    content: str = Field(alias='content')

    tags: typing.Optional[CreateTemplateTags] = Field(None, alias='tags')

    # description of template
    description: typing.Optional[str] = Field(None, alias='description')

    # template inline stylesheet
    stylesheet: typing.Optional[str] = Field(None, alias='stylesheet')

    # type of template
    type: typing.Optional[Literal["DOCUMENT", "EMAIL"]] = Field(None, alias='type')

    # document filename CQL
    filename: typing.Optional[str] = Field(None, alias='filename')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
