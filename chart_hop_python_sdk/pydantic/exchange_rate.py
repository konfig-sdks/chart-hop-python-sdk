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

from chart_hop_python_sdk.pydantic.exchange_rate_rates import ExchangeRateRates

class ExchangeRate(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # date
    date: date = Field(alias='date')

    # base currency
    currency: str = Field(alias='currency')

    rates: ExchangeRateRates = Field(alias='rates')

    # org id, if an org-specific exchange rate is in use
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
