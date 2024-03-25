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

from chart_hop_python_sdk.pydantic.combine_scenario_request_scenario_ids import CombineScenarioRequestScenarioIds

class CombineScenarioRequest(BaseModel):
    scenario_ids: CombineScenarioRequestScenarioIds = Field(alias='scenarioIds')

    copy_only: typing.Optional[bool] = Field(None, alias='copyOnly')

    use_scenario_date_for_changes: typing.Optional[bool] = Field(None, alias='useScenarioDateForChanges')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
