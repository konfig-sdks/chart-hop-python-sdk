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


class StockPrice(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # ticker symbol of this stock
    stock: str = Field(alias='stock')

    # date
    date: date = Field(alias='date')

    # price per share
    price: typing.Union[int, float] = Field(alias='price')

    # type of valuation
    type: Literal["COMMON_FMV", "FUNDRAISE", "GRANT", "PUBLIC"] = Field(alias='type')

    # org id that this stock price derives from
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # total shares outstanding
    total: typing.Optional[int] = Field(None, alias='total')

    # updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # updated by person
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
