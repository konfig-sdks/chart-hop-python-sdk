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


class WelcomeEmailSettings(BaseModel):
    # Subject
    welcome_email_subject: str = Field(alias='welcomeEmailSubject')

    # Button label
    welcome_email_button_label: str = Field(alias='welcomeEmailButtonLabel')

    # Body
    welcome_email_body: str = Field(alias='welcomeEmailBody')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
