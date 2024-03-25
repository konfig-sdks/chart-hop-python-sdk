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

from chart_hop_python_sdk.pydantic.budget_tier_representation_response_reviewees import BudgetTierRepresentationResponseReviewees
from chart_hop_python_sdk.pydantic.job import Job

class BudgetTierRepresentationResponse(BaseModel):
    reviewer: Job = Field(alias='reviewer')

    reviewees: BudgetTierRepresentationResponseReviewees = Field(alias='reviewees')

    eligible: bool = Field(alias='eligible')

    parent_reviewer_job_id: typing.Optional[str] = Field(None, alias='parentReviewerJobId')

    budget: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='budget')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
