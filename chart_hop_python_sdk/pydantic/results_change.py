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
from chart_hop_python_sdk.pydantic.results_access import ResultsAccess

class ResultsChange(BaseModel):
    data: typing.List[Change] = Field(alias='data')

    next: typing.Optional[str] = Field(None, alias='next')

    access: typing.Optional[typing.List[ResultsAccess]] = Field(None, alias='access')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
