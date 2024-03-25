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

from chart_hop_python_sdk.type.get_visualizations_options_change_ids import GetVisualizationsOptionsChangeIds

class RequiredGetVisualizationsOptions(TypedDict):
    # Are the visualizations for a collaborating participant
    isCollabicientView: bool

class OptionalGetVisualizationsOptions(TypedDict, total=False):
    changeIds: GetVisualizationsOptionsChangeIds

    # Currency to view budget visualizations
    viewInCurrency: str

    # Whether or not to include approval requests on which a user is collaborating when calculating budget amounts for that user
    includeCollaborators: bool

class GetVisualizationsOptions(RequiredGetVisualizationsOptions, OptionalGetVisualizationsOptions):
    pass
