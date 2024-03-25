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


class RequiredCancelSubscriptionSurveyAnswers(TypedDict):
    # Any additional comments about ChartHop when cancelling their subscription
    otherComments: str

    # Concatenated string of reasons why the customer unsubscribed from ChartHop
    reason: str

class OptionalCancelSubscriptionSurveyAnswers(TypedDict, total=False):
    pass

class CancelSubscriptionSurveyAnswers(RequiredCancelSubscriptionSurveyAnswers, OptionalCancelSubscriptionSurveyAnswers):
    pass
