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

from chart_hop_python_sdk.pydantic.change import Change
from chart_hop_python_sdk.pydantic.change_data_data import ChangeDataData
from chart_hop_python_sdk.pydantic.change_data_locked_fields import ChangeDataLockedFields

class ChangeData(BaseModel):
    change: Change = Field(alias='change')

    data: ChangeDataData = Field(alias='data')

    # the annualized impact of this change, denoted in organization's currency
    cost: typing.Union[int, float] = Field(alias='cost')

    locked_fields: typing.Optional[ChangeDataLockedFields] = Field(None, alias='lockedFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
