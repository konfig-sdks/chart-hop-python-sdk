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

from chart_hop_python_sdk.type.budget_tier_representation_response_reviewees import BudgetTierRepresentationResponseReviewees
from chart_hop_python_sdk.type.job import Job

class RequiredBudgetTierRepresentationResponse(TypedDict):
    reviewer: Job

    reviewees: BudgetTierRepresentationResponseReviewees

    eligible: bool

class OptionalBudgetTierRepresentationResponse(TypedDict, total=False):
    parentReviewerJobId: str

    budget: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class BudgetTierRepresentationResponse(RequiredBudgetTierRepresentationResponse, OptionalBudgetTierRepresentationResponse):
    pass
