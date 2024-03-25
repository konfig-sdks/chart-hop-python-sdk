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

from chart_hop_python_sdk.type.exchange_rate_rates import ExchangeRateRates

class RequiredExchangeRate(TypedDict):
    # globally unique id
    id: str

    # date
    date: date

    # base currency
    currency: str

    rates: ExchangeRateRates

class OptionalExchangeRate(TypedDict, total=False):
    # org id, if an org-specific exchange rate is in use
    orgId: str

    # updated timestamp
    updateAt: str

class ExchangeRate(RequiredExchangeRate, OptionalExchangeRate):
    pass
