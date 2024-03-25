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


class RequiredStockPrice(TypedDict):
    # globally unique id
    id: str

    # ticker symbol of this stock
    stock: str

    # date
    date: date

    # price per share
    price: typing.Union[int, float]

    # type of valuation
    type: str

class OptionalStockPrice(TypedDict, total=False):
    # org id that this stock price derives from
    orgId: str

    # total shares outstanding
    total: int

    # updated timestamp
    updateAt: str

    # updated by person
    updateId: str

class StockPrice(RequiredStockPrice, OptionalStockPrice):
    pass
