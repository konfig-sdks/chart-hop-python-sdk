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

from chart_hop_python_sdk.pydantic.search_result_search_fields import SearchResultSearchFields

class SearchResult(BaseModel):
    entity: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='entity')

    entity_id: str = Field(alias='entityId')

    entity_type: str = Field(alias='entityType')

    search_fields: SearchResultSearchFields = Field(alias='searchFields')

    score: int = Field(alias='score')

    description: typing.Optional[str] = Field(None, alias='description')

    name: typing.Optional[str] = Field(None, alias='name')

    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
