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


class EmailTemplate(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # name of the email template
    name: str = Field(alias='name')

    # email category
    category: Literal["ADMINISTRATIVE", "BILLING", "DATA_IMPORT_AND_SYNC_STATUS", "TRIAL_REMINDERS"] = Field(alias='category')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )