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

from chart_hop_python_sdk.type.address import Address
from chart_hop_python_sdk.type.product_item import ProductItem

class RequiredCustomer(TypedDict):
    # unique id of customer
    id: str

    # name of customer
    name: str

    # current status
    status: str

class OptionalCustomer(TypedDict, total=False):
    # email address for billing purposes
    email: str

    billAddress: Address

    # industry that customer is in
    industry: str

    # source of customer signup
    source: str

    # stripe customer id
    stripeCustomerId: str

    # salesforce account id
    salesforceAccountId: str

    # products that this customer has purchased
    products: typing.List[ProductItem]

    # initial date of billing
    startDate: date

    # end of service date for churning customers -- on or after this date, service should be disabled
    endDate: date

    # date of next invoice
    nextInvoiceDate: date

    # number of orgs covered by this customer
    orgCount: int

    # number of total headcount across all orgs
    primaryHeadCount: int

    # number of total headcount across all orgs
    secondaryHeadCount: int

    # primary headcount filter - used for billing purposes
    primaryHeadCountFilter: str

    # secondary headcount filter - used for billing purposes
    secondaryHeadCountFilter: str

    # current ARR of the customer based on most recent invoice
    arr: typing.Union[int, float]

    # projected ARR of the customer for upcoming invoice, based on plan and headcount
    projectedArr: typing.Union[int, float]

    # date this customer begins their trial period
    trialStartDate: date

    # date this customer ends their trial period
    trialEndDate: date

    # Stripe subscription settings
    stripeSubscriptionSync: str

    # created timestamp
    createAt: str

    # created by
    createId: str

    # updated timestamp
    updateAt: str

    # updated by
    updateId: str

class Customer(RequiredCustomer, OptionalCustomer):
    pass
