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


class Invoice(BaseModel):
    # a unique identifying string for invoices
    number: str = Field(alias='number')

    # current final amount due for the invoices
    amount: typing.Union[int, float] = Field(alias='amount')

    # one of PAID, UNPAID, or VOID
    status: Literal["PAID", "UNPAID", "VOID"] = Field(alias='status')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # URL for the hosted invoice page, which allows customers to view and pay an invoice
    hosted_invoice_url: typing.Optional[str] = Field(None, alias='hostedInvoiceUrl')

    # the link to download the PDF for the invoice
    invoice_pdf: typing.Optional[str] = Field(None, alias='invoicePdf')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
