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

from chart_hop_python_sdk.pydantic.geopoint import Geopoint

class Address(BaseModel):
    # country (two-digit ISO code)
    country: str = Field(alias='country')

    # street address, line 1
    street1: typing.Optional[str] = Field(None, alias='street1')

    # street address, line 2
    street2: typing.Optional[str] = Field(None, alias='street2')

    # street address, line 3
    street3: typing.Optional[str] = Field(None, alias='street3')

    # city
    city: typing.Optional[str] = Field(None, alias='city')

    # state
    state: typing.Optional[str] = Field(None, alias='state')

    # postal code
    postal: typing.Optional[str] = Field(None, alias='postal')

    geo: typing.Optional[Geopoint] = Field(None, alias='geo')

    approx_geo: typing.Optional[Geopoint] = Field(None, alias='approxGeo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
