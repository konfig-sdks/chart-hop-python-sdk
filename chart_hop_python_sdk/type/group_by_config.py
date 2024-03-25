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

from chart_hop_python_sdk.type.label_override import LabelOverride

class RequiredGroupByConfig(TypedDict):
    pass

class OptionalGroupByConfig(TypedDict, total=False):
    # Overrides by label of label, color, or sort order
    overrides: typing.List[LabelOverride]

    # Maximum number of results to display
    limit: int

    # When combined with limit, whether to include an 'Other' group
    includeOther: bool

    # Whether to include a 'None' group (null values aggregated)
    includeNone: bool

    # When combined with fieldId or questionId, will include all values from that fieldId or questionId, even if none of them were used
    includeAllValues: bool

    # The field to use to retrieve values, when includeAllValues is in use
    fieldId: str

    # The question to use to retrieve values, when includeAllValues is in use
    questionId: str

    # Whether to sort the results -- by default, will sort by label if there is no limit, will sort by value descending if there is a limit
    sortBy: str

    # The direction to sort the results
    sortDirection: str

class GroupByConfig(RequiredGroupByConfig, OptionalGroupByConfig):
    pass
