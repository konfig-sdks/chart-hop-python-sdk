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

from chart_hop_python_sdk.type.search_result_search_fields import SearchResultSearchFields

class RequiredSearchResult(TypedDict):
    entity: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    entityId: str

    entityType: str

    searchFields: SearchResultSearchFields

    score: int

class OptionalSearchResult(TypedDict, total=False):
    description: str

    name: str

    imagePath: str

class SearchResult(RequiredSearchResult, OptionalSearchResult):
    pass
