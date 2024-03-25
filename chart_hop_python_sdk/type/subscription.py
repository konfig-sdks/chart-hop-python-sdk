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

from chart_hop_python_sdk.type.payment_info import PaymentInfo
from chart_hop_python_sdk.type.plan import Plan

class RequiredSubscription(TypedDict):
    # Timestamp when the next invoice will be generated
    nextInvoiceAt: str

    plan: Plan

    paymentInfo: PaymentInfo

class OptionalSubscription(TypedDict, total=False):
    pass

class Subscription(RequiredSubscription, OptionalSubscription):
    pass
