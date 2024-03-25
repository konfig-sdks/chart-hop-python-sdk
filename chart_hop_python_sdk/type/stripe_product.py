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


class RequiredStripeProduct(TypedDict):
    # unique Stripe identifier for this product
    stripeId: str

    # human-readable nickname for this product
    label: str

class OptionalStripeProduct(TypedDict, total=False):
    pass

class StripeProduct(RequiredStripeProduct, OptionalStripeProduct):
    pass
