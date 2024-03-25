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


class QueryToken(BaseModel):
    # globally unique id for query token
    id: str = Field(alias='id')

    # globally unique random token string
    token: str = Field(alias='token')

    # id of org
    org_id: str = Field(alias='orgId')

    # id of user
    user_id: str = Field(alias='userId')

    # query type
    type: str = Field(alias='type')

    # query params
    params: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='params')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # expire timestamp
    expire_at: str = Field(alias='expireAt')

    # query path (deprecated)
    path: typing.Optional[str] = Field(None, alias='path')

    # total number of uses
    access_count: typing.Optional[int] = Field(None, alias='accessCount')

    # last active timestamp
    active_at: typing.Optional[str] = Field(None, alias='activeAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
