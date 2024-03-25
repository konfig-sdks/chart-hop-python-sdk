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

from chart_hop_python_sdk.type.comp_review_config import CompReviewConfig
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredUpdateCompReview(TypedDict):
    pass

class OptionalUpdateCompReview(TypedDict, total=False):
    # human-readable label of goal
    label: str

    config: CompReviewConfig

    # Whether the compensation review has been approved by the final approvers
    status: str

    # users who have been granted access to this comp review
    shareAccess: typing.List[ShareAccess]

    # count of reviewers in the comp review
    reviewerCount: int

    # count of reviews that have been submitted and approved
    submittedCount: int

class UpdateCompReview(RequiredUpdateCompReview, OptionalUpdateCompReview):
    pass
