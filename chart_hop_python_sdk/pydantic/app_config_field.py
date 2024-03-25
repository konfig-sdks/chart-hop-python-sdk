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

from chart_hop_python_sdk.pydantic.app_config_field_required_fields import AppConfigFieldRequiredFields

class AppConfigField(BaseModel):
    name: str = Field(alias='name')

    label: str = Field(alias='label')

    type: Literal["STRING", "SUBDOMAIN", "URL", "SECRET", "XML", "OAUTH", "INSTRUCTION"] = Field(alias='type')

    details: typing.Optional[str] = Field(None, alias='details')

    subdomain: typing.Optional[str] = Field(None, alias='subdomain')

    optional: typing.Optional[bool] = Field(None, alias='optional')

    config_section: typing.Optional[str] = Field(None, alias='configSection')

    oauth_url: typing.Optional[str] = Field(None, alias='oauthUrl')

    required_fields: typing.Optional[AppConfigFieldRequiredFields] = Field(None, alias='requiredFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
