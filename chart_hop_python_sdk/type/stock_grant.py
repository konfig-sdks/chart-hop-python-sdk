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

from chart_hop_python_sdk.type.stock_grant_vested_shares_by_date import StockGrantVestedSharesByDate

class RequiredStockGrant(TypedDict):
    # unique identifier of grant
    id: str

    # ticker symbol of this stock
    stock: str

    # date of grant
    date: date

    # number of shares granted
    shares: typing.Union[int, float]

    # per share strike price
    price: typing.Union[int, float]

    # type of grant
    type: str

    # vesting schedule
    vestSchedule: str

class OptionalStockGrant(TypedDict, total=False):
    # human-readable description of vesting schedule
    description: str

    # vesting start date of grant
    vestStartDate: date

    # expiration date of grant
    expireDate: date

    # original per share value of stock (grant price at time of issue)
    originalPrice: typing.Union[int, float]

    # current per share value of stock
    currentPrice: typing.Union[int, float]

    # current number of shares vested
    vestedShares: typing.Union[int, float]

    # number of shares vested one year from today
    vestedSharesNextYear: typing.Union[int, float]

    vestedSharesByDate: StockGrantVestedSharesByDate

    # vesting end date
    vestEndDate: date

    # cancellation date
    cancelDate: date

    # details of the grant (arbitrary text)
    details: str

class StockGrant(RequiredStockGrant, OptionalStockGrant):
    pass
