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

from chart_hop_python_sdk.pydantic.in_cycle_view_changes_change_map import InCycleViewChangesChangeMap
from chart_hop_python_sdk.pydantic.in_cycle_view_changes_guidelines_map import InCycleViewChangesGuidelinesMap

class InCycleViewChanges(BaseModel):
    change_map: InCycleViewChangesChangeMap = Field(alias='changeMap')

    guidelines_map: typing.Optional[InCycleViewChangesGuidelinesMap] = Field(None, alias='guidelinesMap')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
