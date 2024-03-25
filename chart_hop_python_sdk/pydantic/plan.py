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

from chart_hop_python_sdk.pydantic.plan_tier import PlanTier

class Plan(BaseModel):
    # unique Stripe identifier for this plan
    id: str = Field(alias='id')

    # human-readable nickname for this plan
    name: str = Field(alias='name')

    # interval for billing on this plan
    interval: Literal["DAY", "WEEK", "MONTH", "YEAR"] = Field(alias='interval')

    # number of intervals, for example 3 for quarterly billing
    interval_count: int = Field(alias='intervalCount')

    # pricing tiers, per employee per interval
    tiers: typing.List[PlanTier] = Field(alias='tiers')

    # stripe product id that this plan belongs to
    stripe_product_id: str = Field(alias='stripeProductId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
