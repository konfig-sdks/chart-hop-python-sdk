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

from chart_hop_python_sdk.pydantic.stock_grant_vested_shares_by_date import StockGrantVestedSharesByDate

class StockGrant(BaseModel):
    # unique identifier of grant
    id: str = Field(alias='id')

    # ticker symbol of this stock
    stock: str = Field(alias='stock')

    # date of grant
    date: date = Field(alias='date')

    # number of shares granted
    shares: typing.Union[int, float] = Field(alias='shares')

    # per share strike price
    price: typing.Union[int, float] = Field(alias='price')

    # type of grant
    type: Literal["ISO", "NSO", "RSU", "SAR", "PERFORMANCE_SHARES", "PHANTOM_STOCK", "RSA"] = Field(alias='type')

    # vesting schedule
    vest_schedule: str = Field(alias='vestSchedule')

    # human-readable description of vesting schedule
    description: typing.Optional[str] = Field(None, alias='description')

    # vesting start date of grant
    vest_start_date: typing.Optional[date] = Field(None, alias='vestStartDate')

    # expiration date of grant
    expire_date: typing.Optional[date] = Field(None, alias='expireDate')

    # original per share value of stock (grant price at time of issue)
    original_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='originalPrice')

    # current per share value of stock
    current_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentPrice')

    # current number of shares vested
    vested_shares: typing.Optional[typing.Union[int, float]] = Field(None, alias='vestedShares')

    # number of shares vested one year from today
    vested_shares_next_year: typing.Optional[typing.Union[int, float]] = Field(None, alias='vestedSharesNextYear')

    vested_shares_by_date: typing.Optional[StockGrantVestedSharesByDate] = Field(None, alias='vestedSharesByDate')

    # vesting end date
    vest_end_date: typing.Optional[date] = Field(None, alias='vestEndDate')

    # cancellation date
    cancel_date: typing.Optional[date] = Field(None, alias='cancelDate')

    # details of the grant (arbitrary text)
    details: typing.Optional[str] = Field(None, alias='details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
