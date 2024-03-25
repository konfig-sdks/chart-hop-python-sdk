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


class Agreement(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # action taken
    action: str = Field(alias='action')

    # timestamp that the agreement was accepted/cancelled
    create_at: str = Field(alias='createAt')

    # user id who accepted/cancelled the agreement
    create_id: str = Field(alias='createId')

    # legal document entity id
    legal_doc_id: typing.Optional[str] = Field(None, alias='legalDocId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
