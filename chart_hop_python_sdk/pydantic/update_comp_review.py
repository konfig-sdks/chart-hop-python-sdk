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

from chart_hop_python_sdk.pydantic.comp_review_config import CompReviewConfig
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class UpdateCompReview(BaseModel):
    # human-readable label of goal
    label: typing.Optional[str] = Field(None, alias='label')

    config: typing.Optional[CompReviewConfig] = Field(None, alias='config')

    # Whether the compensation review has been approved by the final approvers
    status: typing.Optional[Literal["PENDING", "PAUSED", "ACTIVE", "REJECTED", "COMPLETE", "COMPLETE_APPROVED"]] = Field(None, alias='status')

    # users who have been granted access to this comp review
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # count of reviewers in the comp review
    reviewer_count: typing.Optional[int] = Field(None, alias='reviewerCount')

    # count of reviews that have been submitted and approved
    submitted_count: typing.Optional[int] = Field(None, alias='submittedCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
