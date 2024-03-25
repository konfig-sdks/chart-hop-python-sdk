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

from chart_hop_python_sdk.pydantic.label_override import LabelOverride

class GroupByConfig(BaseModel):
    # Overrides by label of label, color, or sort order
    overrides: typing.Optional[typing.List[LabelOverride]] = Field(None, alias='overrides')

    # Maximum number of results to display
    limit: typing.Optional[int] = Field(None, alias='limit')

    # When combined with limit, whether to include an 'Other' group
    include_other: typing.Optional[bool] = Field(None, alias='includeOther')

    # Whether to include a 'None' group (null values aggregated)
    include_none: typing.Optional[bool] = Field(None, alias='includeNone')

    # When combined with fieldId or questionId, will include all values from that fieldId or questionId, even if none of them were used
    include_all_values: typing.Optional[bool] = Field(None, alias='includeAllValues')

    # The field to use to retrieve values, when includeAllValues is in use
    field_id: typing.Optional[str] = Field(None, alias='fieldId')

    # The question to use to retrieve values, when includeAllValues is in use
    question_id: typing.Optional[str] = Field(None, alias='questionId')

    # Whether to sort the results -- by default, will sort by label if there is no limit, will sort by value descending if there is a limit
    sort_by: typing.Optional[Literal["LABEL", "KEY", "VALUE", "COUNT"]] = Field(None, alias='sortBy')

    # The direction to sort the results
    sort_direction: typing.Optional[Literal["ASC", "DESC"]] = Field(None, alias='sortDirection')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
