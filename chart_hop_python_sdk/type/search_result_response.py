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

from chart_hop_python_sdk.type.search_result import SearchResult

class RequiredSearchResultResponse(TypedDict):
    pass

class OptionalSearchResultResponse(TypedDict, total=False):
    orgs: typing.List[SearchResult]

    customers: typing.List[SearchResult]

    jobs: typing.List[SearchResult]

    persons: typing.List[SearchResult]

    groups: typing.List[SearchResult]

    fields: typing.List[SearchResult]

    functions: typing.List[SearchResult]

    reports: typing.List[SearchResult]

    scenarios: typing.List[SearchResult]

    users: typing.List[SearchResult]

    appUsers: typing.List[SearchResult]

    compBands: typing.List[SearchResult]

    questions: typing.List[SearchResult]

    contents: typing.List[SearchResult]

class SearchResultResponse(RequiredSearchResultResponse, OptionalSearchResultResponse):
    pass
