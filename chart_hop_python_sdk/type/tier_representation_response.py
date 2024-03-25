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

from chart_hop_python_sdk.type.job import Job
from chart_hop_python_sdk.type.tier_representation_response_reviewees import TierRepresentationResponseReviewees

class RequiredTierRepresentationResponse(TypedDict):
    reviewer: Job

    reviewees: TierRepresentationResponseReviewees

    eligible: bool

class OptionalTierRepresentationResponse(TypedDict, total=False):
    parentReviewerJobId: str

class TierRepresentationResponse(RequiredTierRepresentationResponse, OptionalTierRepresentationResponse):
    pass
