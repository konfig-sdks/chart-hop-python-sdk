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


class RequiredUpdateStockPrice(TypedDict):
    pass

class OptionalUpdateStockPrice(TypedDict, total=False):
    # org id that this stock price derives from
    orgId: str

    # price per share
    price: typing.Union[int, float]

    # total shares outstanding
    total: int

class UpdateStockPrice(RequiredUpdateStockPrice, OptionalUpdateStockPrice):
    pass
