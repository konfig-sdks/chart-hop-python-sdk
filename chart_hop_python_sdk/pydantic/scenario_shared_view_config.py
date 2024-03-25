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

from chart_hop_python_sdk.pydantic.scenario_shared_view_config_column_widths import ScenarioSharedViewConfigColumnWidths
from chart_hop_python_sdk.pydantic.scenario_shared_view_config_custom_column_names import ScenarioSharedViewConfigCustomColumnNames

class ScenarioSharedViewConfig(BaseModel):
    custom_column_names: typing.Optional[ScenarioSharedViewConfigCustomColumnNames] = Field(None, alias='customColumnNames')

    column_widths: typing.Optional[ScenarioSharedViewConfigColumnWidths] = Field(None, alias='columnWidths')

    # type of view
    type: typing.Optional[Literal["ALL_CHANGES_GROUPED"]] = Field(None, alias='type')

    # update id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # update at
    update_at: typing.Optional[int] = Field(None, alias='updateAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
