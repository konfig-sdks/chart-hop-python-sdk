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

from chart_hop_python_sdk.pydantic.comp_review_reviewers_approvers_approver_ids import CompReviewReviewersApproversApproverIds
from chart_hop_python_sdk.pydantic.comp_review_reviewers_approvers_excluded_reviewer_ids import CompReviewReviewersApproversExcludedReviewerIds
from chart_hop_python_sdk.pydantic.comp_review_reviewers_approvers_reviewer_levels import CompReviewReviewersApproversReviewerLevels
from chart_hop_python_sdk.pydantic.comp_review_reviewers_approvers_reviewer_titles import CompReviewReviewersApproversReviewerTitles

class CompReviewReviewersApprovers(BaseModel):
    # Which individuals are included as reviewers
    reviewers: Literal["ALL_MANAGERS", "ONLY_SPECIFIC_LEVEL", "ONLY_SPECIFIC_TITLES", "CUSTOM"] = Field(alias='reviewers')

    reviewer_levels: typing.Optional[CompReviewReviewersApproversReviewerLevels] = Field(None, alias='reviewerLevels')

    reviewer_titles: typing.Optional[CompReviewReviewersApproversReviewerTitles] = Field(None, alias='reviewerTitles')

    # Filter to be applied if reviewers is custom
    reviewer_filter: typing.Optional[str] = Field(None, alias='reviewerFilter')

    excluded_reviewer_ids: typing.Optional[CompReviewReviewersApproversExcludedReviewerIds] = Field(None, alias='excludedReviewerIds')

    approver_ids: typing.Optional[CompReviewReviewersApproversApproverIds] = Field(None, alias='approverIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
