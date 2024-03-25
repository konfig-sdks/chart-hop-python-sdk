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


class UserEmailSetting(BaseModel):
    # Category of emails
    category: Literal["ADMINISTRATIVE", "BILLING", "DATA_IMPORT_AND_SYNC_STATUS", "TRIAL_REMINDERS"] = Field(alias='category')

    # Is user subscribed to the category of emails
    subscribed: bool = Field(alias='subscribed')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
