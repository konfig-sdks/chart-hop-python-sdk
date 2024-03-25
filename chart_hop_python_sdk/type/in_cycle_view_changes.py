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

from chart_hop_python_sdk.type.in_cycle_view_changes_change_map import InCycleViewChangesChangeMap
from chart_hop_python_sdk.type.in_cycle_view_changes_guidelines_map import InCycleViewChangesGuidelinesMap

class RequiredInCycleViewChanges(TypedDict):
    changeMap: InCycleViewChangesChangeMap

class OptionalInCycleViewChanges(TypedDict, total=False):
    guidelinesMap: InCycleViewChangesGuidelinesMap

class InCycleViewChanges(RequiredInCycleViewChanges, OptionalInCycleViewChanges):
    pass
