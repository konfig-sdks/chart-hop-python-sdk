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

from chart_hop_python_sdk.type.plan_tier import PlanTier

class RequiredPlan(TypedDict):
    # unique Stripe identifier for this plan
    id: str

    # human-readable nickname for this plan
    name: str

    # interval for billing on this plan
    interval: str

    # number of intervals, for example 3 for quarterly billing
    intervalCount: int

    # pricing tiers, per employee per interval
    tiers: typing.List[PlanTier]

    # stripe product id that this plan belongs to
    stripeProductId: str

class OptionalPlan(TypedDict, total=False):
    pass

class Plan(RequiredPlan, OptionalPlan):
    pass
