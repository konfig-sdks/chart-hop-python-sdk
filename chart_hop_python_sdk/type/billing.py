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

from chart_hop_python_sdk.type.checkout import Checkout
from chart_hop_python_sdk.type.customer import Customer
from chart_hop_python_sdk.type.invoice import Invoice
from chart_hop_python_sdk.type.org import Org
from chart_hop_python_sdk.type.payment_info import PaymentInfo
from chart_hop_python_sdk.type.plan import Plan

class RequiredBilling(TypedDict):
    customer: Customer

    invoices: typing.List[Invoice]

    org: Org

class OptionalBilling(TypedDict, total=False):
    checkout: Checkout

    paymentInfo: PaymentInfo

    plan: Plan

class Billing(RequiredBilling, OptionalBilling):
    pass
