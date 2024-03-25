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

from chart_hop_python_sdk.type.app_config_field_required_fields import AppConfigFieldRequiredFields

class RequiredAppConfigField(TypedDict):
    name: str

    label: str

    type: str

class OptionalAppConfigField(TypedDict, total=False):
    details: str

    subdomain: str

    optional: bool

    configSection: str

    oauthUrl: str

    requiredFields: AppConfigFieldRequiredFields

class AppConfigField(RequiredAppConfigField, OptionalAppConfigField):
    pass
