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


class RequiredInvoice(TypedDict):
    # a unique identifying string for invoices
    number: str

    # current final amount due for the invoices
    amount: typing.Union[int, float]

    # one of PAID, UNPAID, or VOID
    status: str

    # created timestamp
    createAt: str

class OptionalInvoice(TypedDict, total=False):
    # URL for the hosted invoice page, which allows customers to view and pay an invoice
    hostedInvoiceUrl: str

    # the link to download the PDF for the invoice
    invoicePdf: str

class Invoice(RequiredInvoice, OptionalInvoice):
    pass
