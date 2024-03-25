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

from chart_hop_python_sdk.pydantic.create_action import CreateAction
from chart_hop_python_sdk.pydantic.partial_task_config import PartialTaskConfig

class CreateActionBody(BaseModel):
    action: CreateAction = Field(alias='action')

    step_task_configs: typing.Optional[typing.List[PartialTaskConfig]] = Field(None, alias='stepTaskConfigs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
