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

from chart_hop_python_sdk.type.stock_price import StockPrice

class RequiredResultsStockPrice(TypedDict):
    data: typing.List[StockPrice]

class OptionalResultsStockPrice(TypedDict, total=False):
    next: str

class ResultsStockPrice(RequiredResultsStockPrice, OptionalResultsStockPrice):
    pass