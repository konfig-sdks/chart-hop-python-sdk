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


class PaymentInfo(BaseModel):
    # indicates how the customer has decided to pay; one of CREDIT_CARD, INVOICE
    payment_type: Literal["CREDIT_CARD", "INVOICE"] = Field(alias='paymentType')

    # if the customer has indicated they wish to pay by credit card, the last four digits of the credit card they are paying with. Null if the customer is paying by invoice.
    credit_card_end_digits: typing.Optional[str] = Field(None, alias='creditCardEndDigits')

    # if the customer has indicated they wish to pay by credit card, the brand of the credit card they are paying with. Null if the customer is paying by invoice.
    brand: typing.Optional[str] = Field(None, alias='brand')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
