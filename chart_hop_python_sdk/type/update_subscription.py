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


class RequiredUpdateSubscription(TypedDict):
    # Payment method to create; 'INVOICE' to make subscription paid by invoice, or the ID of the payment method if to make the subscription automatically charge a card
    paymentMethod: str

class OptionalUpdateSubscription(TypedDict, total=False):
    pass

class UpdateSubscription(RequiredUpdateSubscription, OptionalUpdateSubscription):
    pass
