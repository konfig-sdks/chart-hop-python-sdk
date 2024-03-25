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

from chart_hop_python_sdk.pydantic.checkout import Checkout
from chart_hop_python_sdk.pydantic.customer import Customer
from chart_hop_python_sdk.pydantic.invoice import Invoice
from chart_hop_python_sdk.pydantic.org import Org
from chart_hop_python_sdk.pydantic.payment_info import PaymentInfo
from chart_hop_python_sdk.pydantic.plan import Plan

class Billing(BaseModel):
    customer: Customer = Field(alias='customer')

    invoices: typing.List[Invoice] = Field(alias='invoices')

    org: Org = Field(alias='org')

    checkout: typing.Optional[Checkout] = Field(None, alias='checkout')

    payment_info: typing.Optional[PaymentInfo] = Field(None, alias='paymentInfo')

    plan: typing.Optional[Plan] = Field(None, alias='plan')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
