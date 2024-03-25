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


class GrantAlias(BaseModel):
    grant_type: Literal["ISO", "NSO", "RSU", "SAR", "PERFORMANCE_SHARES", "PHANTOM_STOCK", "RSA"] = Field(alias='grantType')

    enabled: bool = Field(alias='enabled')

    alias: typing.Optional[str] = Field(None, alias='alias')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
