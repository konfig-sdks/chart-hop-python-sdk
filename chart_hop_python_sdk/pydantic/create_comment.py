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

from chart_hop_python_sdk.pydantic.markup import Markup

class CreateComment(BaseModel):
    # entity the comment was posted on
    entity_id: str = Field(alias='entityId')

    # type of entity the comment was posted on
    entity_type: Literal["CHANGE", "ASSESSMENT", "SCENARIO", "APPROVAL_APPROVE", "APPROVAL_REJECT", "APPROVAL_REASSIGN", "APPROVAL_WITHDRAW"] = Field(alias='entityType')

    content: Markup = Field(alias='content')

    # parent entity id that this comment belongs to, should be used with entityId
    parent_entity_id: typing.Optional[str] = Field(None, alias='parentEntityId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
