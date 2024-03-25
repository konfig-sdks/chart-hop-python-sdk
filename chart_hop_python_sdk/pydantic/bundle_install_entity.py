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


class BundleInstallEntity(BaseModel):
    entity_type: Literal["ACTION", "CATEGORY", "FIELD", "FORM", "GROUP", "PROFILE_TAB", "QUESTION", "REPORT", "REPORT_CHART", "TASK_CONFIG", "TEMPLATE", "CONTENT"] = Field(alias='entityType')

    entity_id: str = Field(alias='entityId')

    original_id: str = Field(alias='originalId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
