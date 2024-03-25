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

from chart_hop_python_sdk.pydantic.payment_info import PaymentInfo
from chart_hop_python_sdk.pydantic.plan import Plan

class Subscription(BaseModel):
    # Timestamp when the next invoice will be generated
    next_invoice_at: str = Field(alias='nextInvoiceAt')

    plan: Plan = Field(alias='plan')

    payment_info: PaymentInfo = Field(alias='paymentInfo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
