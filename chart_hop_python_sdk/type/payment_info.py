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


class RequiredPaymentInfo(TypedDict):
    # indicates how the customer has decided to pay; one of CREDIT_CARD, INVOICE
    paymentType: str

class OptionalPaymentInfo(TypedDict, total=False):
    # if the customer has indicated they wish to pay by credit card, the last four digits of the credit card they are paying with. Null if the customer is paying by invoice.
    creditCardEndDigits: str

    # if the customer has indicated they wish to pay by credit card, the brand of the credit card they are paying with. Null if the customer is paying by invoice.
    brand: str

class PaymentInfo(RequiredPaymentInfo, OptionalPaymentInfo):
    pass
