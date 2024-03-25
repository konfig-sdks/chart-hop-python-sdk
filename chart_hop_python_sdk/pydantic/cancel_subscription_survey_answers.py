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


class CancelSubscriptionSurveyAnswers(BaseModel):
    # Any additional comments about ChartHop when cancelling their subscription
    other_comments: str = Field(alias='otherComments')

    # Concatenated string of reasons why the customer unsubscribed from ChartHop
    reason: str = Field(alias='reason')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )