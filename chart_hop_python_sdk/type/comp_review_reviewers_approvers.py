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

from chart_hop_python_sdk.type.comp_review_reviewers_approvers_approver_ids import CompReviewReviewersApproversApproverIds
from chart_hop_python_sdk.type.comp_review_reviewers_approvers_excluded_reviewer_ids import CompReviewReviewersApproversExcludedReviewerIds
from chart_hop_python_sdk.type.comp_review_reviewers_approvers_reviewer_levels import CompReviewReviewersApproversReviewerLevels
from chart_hop_python_sdk.type.comp_review_reviewers_approvers_reviewer_titles import CompReviewReviewersApproversReviewerTitles

class RequiredCompReviewReviewersApprovers(TypedDict):
    # Which individuals are included as reviewers
    reviewers: str

class OptionalCompReviewReviewersApprovers(TypedDict, total=False):
    reviewerLevels: CompReviewReviewersApproversReviewerLevels

    reviewerTitles: CompReviewReviewersApproversReviewerTitles

    # Filter to be applied if reviewers is custom
    reviewerFilter: str

    excludedReviewerIds: CompReviewReviewersApproversExcludedReviewerIds

    approverIds: CompReviewReviewersApproversApproverIds

class CompReviewReviewersApprovers(RequiredCompReviewReviewersApprovers, OptionalCompReviewReviewersApprovers):
    pass
