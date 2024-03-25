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

from chart_hop_python_sdk.type.comp_review_workbook_column_visible_to_groups import CompReviewWorkbookColumnVisibleToGroups
from chart_hop_python_sdk.type.in_cycle_view_features import InCycleViewFeatures

class RequiredCompReviewWorkbookColumn(TypedDict):
    # field name
    name: str

    # display name in workbook
    label: str

    # cql evaluated on the reviewee job specifying whether field is editable
    editableFor: str

    # cql specifying who can view
    visibleTo: str

    visibleToGroups: CompReviewWorkbookColumnVisibleToGroups

    # type of cql filter used in the visible to
    visibleToType: str

class OptionalCompReviewWorkbookColumn(TypedDict, total=False):
    # color used in the column header
    color: str

    visibleToRoles: InCycleViewFeatures

class CompReviewWorkbookColumn(RequiredCompReviewWorkbookColumn, OptionalCompReviewWorkbookColumn):
    pass
