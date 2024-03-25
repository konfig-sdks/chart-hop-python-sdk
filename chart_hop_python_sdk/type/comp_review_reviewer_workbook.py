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

from chart_hop_python_sdk.type.comp_review_workbook_column import CompReviewWorkbookColumn

class RequiredCompReviewReviewerWorkbook(TypedDict):
    # ordering and settings of columns in workbook
    columns: typing.List[CompReviewWorkbookColumn]

class OptionalCompReviewReviewerWorkbook(TypedDict, total=False):
    # number of frozen columns at start of workbook
    numFrozenColumns: int

    # optional link to see additional customer documentation
    moreInfoUrl: str

    # optional label for additional customer documentation
    moreInfoLabel: str

    # whether the default config has been modified
    isEdited: bool

class CompReviewReviewerWorkbook(RequiredCompReviewReviewerWorkbook, OptionalCompReviewReviewerWorkbook):
    pass
