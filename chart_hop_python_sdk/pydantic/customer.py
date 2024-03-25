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

from chart_hop_python_sdk.pydantic.address import Address
from chart_hop_python_sdk.pydantic.product_item import ProductItem

class Customer(BaseModel):
    # unique id of customer
    id: str = Field(alias='id')

    # name of customer
    name: str = Field(alias='name')

    # current status
    status: Literal["ACTIVE", "INACTIVE", "TRIAL", "CHURN", "PAYMENT_ERROR"] = Field(alias='status')

    # email address for billing purposes
    email: typing.Optional[str] = Field(None, alias='email')

    bill_address: typing.Optional[Address] = Field(None, alias='billAddress')

    # industry that customer is in
    industry: typing.Optional[str] = Field(None, alias='industry')

    # source of customer signup
    source: typing.Optional[Literal["ADP_MARKETPLACE", "SELF_SERVE", "SELF_SERVE_TEST", "SEQUOIA_ONE", "CONNECT"]] = Field(None, alias='source')

    # stripe customer id
    stripe_customer_id: typing.Optional[str] = Field(None, alias='stripeCustomerId')

    # salesforce account id
    salesforce_account_id: typing.Optional[str] = Field(None, alias='salesforceAccountId')

    # products that this customer has purchased
    products: typing.Optional[typing.List[ProductItem]] = Field(None, alias='products')

    # initial date of billing
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    # end of service date for churning customers -- on or after this date, service should be disabled
    end_date: typing.Optional[date] = Field(None, alias='endDate')

    # date of next invoice
    next_invoice_date: typing.Optional[date] = Field(None, alias='nextInvoiceDate')

    # number of orgs covered by this customer
    org_count: typing.Optional[int] = Field(None, alias='orgCount')

    # number of total headcount across all orgs
    primary_head_count: typing.Optional[int] = Field(None, alias='primaryHeadCount')

    # number of total headcount across all orgs
    secondary_head_count: typing.Optional[int] = Field(None, alias='secondaryHeadCount')

    # primary headcount filter - used for billing purposes
    primary_head_count_filter: typing.Optional[str] = Field(None, alias='primaryHeadCountFilter')

    # secondary headcount filter - used for billing purposes
    secondary_head_count_filter: typing.Optional[str] = Field(None, alias='secondaryHeadCountFilter')

    # current ARR of the customer based on most recent invoice
    arr: typing.Optional[typing.Union[int, float]] = Field(None, alias='arr')

    # projected ARR of the customer for upcoming invoice, based on plan and headcount
    projected_arr: typing.Optional[typing.Union[int, float]] = Field(None, alias='projectedArr')

    # date this customer begins their trial period
    trial_start_date: typing.Optional[date] = Field(None, alias='trialStartDate')

    # date this customer ends their trial period
    trial_end_date: typing.Optional[date] = Field(None, alias='trialEndDate')

    # Stripe subscription settings
    stripe_subscription_sync: typing.Optional[Literal["SYNC", "DELETE"]] = Field(None, alias='stripeSubscriptionSync')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # created by
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # updated by
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
