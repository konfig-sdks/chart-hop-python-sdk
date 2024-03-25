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


class SmartCurrencyOption(BaseModel):
    # codename for the option
    name: Literal["PERSON_HOME_ADDRESS_COUNTRY", "JOB_LOCATION_COUNTRY", "JOB_CURRENCY"] = Field(alias='name')

    # determines if this option should be used
    enabled: bool = Field(alias='enabled')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
