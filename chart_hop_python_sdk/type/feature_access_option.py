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


class RequiredFeatureAccessOption(TypedDict):
    # The name of the feature option tied to the feature access
    name: str

    # The feature option type
    type: str

class OptionalFeatureAccessOption(TypedDict, total=False):
    # The description of the feature option
    description: str

    # The feature option limit
    limit: int

class FeatureAccessOption(RequiredFeatureAccessOption, OptionalFeatureAccessOption):
    pass
