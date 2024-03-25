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


class OrgStockData(BaseModel):
    strike_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='strikePrice')

    grant_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='grantPrice')

    total_shares: typing.Optional[int] = Field(None, alias='totalShares')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
