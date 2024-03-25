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

from chart_hop_python_sdk.pydantic.search_result import SearchResult

class SearchResultResponse(BaseModel):
    orgs: typing.Optional[typing.List[SearchResult]] = Field(None, alias='orgs')

    customers: typing.Optional[typing.List[SearchResult]] = Field(None, alias='customers')

    jobs: typing.Optional[typing.List[SearchResult]] = Field(None, alias='jobs')

    persons: typing.Optional[typing.List[SearchResult]] = Field(None, alias='persons')

    groups: typing.Optional[typing.List[SearchResult]] = Field(None, alias='groups')

    fields: typing.Optional[typing.List[SearchResult]] = Field(None, alias='fields')

    functions: typing.Optional[typing.List[SearchResult]] = Field(None, alias='functions')

    reports: typing.Optional[typing.List[SearchResult]] = Field(None, alias='reports')

    scenarios: typing.Optional[typing.List[SearchResult]] = Field(None, alias='scenarios')

    users: typing.Optional[typing.List[SearchResult]] = Field(None, alias='users')

    app_users: typing.Optional[typing.List[SearchResult]] = Field(None, alias='appUsers')

    comp_bands: typing.Optional[typing.List[SearchResult]] = Field(None, alias='compBands')

    questions: typing.Optional[typing.List[SearchResult]] = Field(None, alias='questions')

    contents: typing.Optional[typing.List[SearchResult]] = Field(None, alias='contents')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
