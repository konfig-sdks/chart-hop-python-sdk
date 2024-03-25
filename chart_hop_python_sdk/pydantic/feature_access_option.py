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


class FeatureAccessOption(BaseModel):
    # The name of the feature option tied to the feature access
    name: Literal["CONFIGURED_ROLES", "SMART_FIELDS", "APP_FIELD_MAPPERS", "MULTI_PAYROLL_INSTALLS"] = Field(alias='name')

    # The feature option type
    type: Literal["LIMIT", "FULL_ACCESS"] = Field(alias='type')

    # The description of the feature option
    description: typing.Optional[str] = Field(None, alias='description')

    # The feature option limit
    limit: typing.Optional[int] = Field(None, alias='limit')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
