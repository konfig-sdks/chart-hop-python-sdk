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

from chart_hop_python_sdk.pydantic.get_visualizations_options_change_ids import GetVisualizationsOptionsChangeIds

class GetVisualizationsOptions(BaseModel):
    # Are the visualizations for a collaborating participant
    is_collabicient_view: bool = Field(alias='isCollabicientView')

    change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = Field(None, alias='changeIds')

    # Currency to view budget visualizations
    view_in_currency: typing.Optional[str] = Field(None, alias='viewInCurrency')

    # Whether or not to include approval requests on which a user is collaborating when calculating budget amounts for that user
    include_collaborators: typing.Optional[bool] = Field(None, alias='includeCollaborators')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
