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

from chart_hop_python_sdk.pydantic.comp_review_workbook_column import CompReviewWorkbookColumn

class CompReviewReviewerWorkbook(BaseModel):
    # ordering and settings of columns in workbook
    columns: typing.List[CompReviewWorkbookColumn] = Field(alias='columns')

    # number of frozen columns at start of workbook
    num_frozen_columns: typing.Optional[int] = Field(None, alias='numFrozenColumns')

    # optional link to see additional customer documentation
    more_info_url: typing.Optional[str] = Field(None, alias='moreInfoUrl')

    # optional label for additional customer documentation
    more_info_label: typing.Optional[str] = Field(None, alias='moreInfoLabel')

    # whether the default config has been modified
    is_edited: typing.Optional[bool] = Field(None, alias='isEdited')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
