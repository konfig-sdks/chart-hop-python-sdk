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

from chart_hop_python_sdk.pydantic.comp_review_workbook_column_visible_to_groups import CompReviewWorkbookColumnVisibleToGroups
from chart_hop_python_sdk.pydantic.in_cycle_view_features import InCycleViewFeatures

class CompReviewWorkbookColumn(BaseModel):
    # field name
    name: str = Field(alias='name')

    # display name in workbook
    label: str = Field(alias='label')

    # cql evaluated on the reviewee job specifying whether field is editable
    editable_for: str = Field(alias='editableFor')

    # cql specifying who can view
    visible_to: str = Field(alias='visibleTo')

    visible_to_groups: CompReviewWorkbookColumnVisibleToGroups = Field(alias='visibleToGroups')

    # type of cql filter used in the visible to
    visible_to_type: Literal["EVERYONE", "DEPARTMENT", "TEAM", "LOCATION", "CUSTOM"] = Field(alias='visibleToType')

    # color used in the column header
    color: typing.Optional[str] = Field(None, alias='color')

    visible_to_roles: typing.Optional[InCycleViewFeatures] = Field(None, alias='visibleToRoles')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
