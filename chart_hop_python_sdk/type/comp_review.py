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

class RequiredCompReview(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable label of goal
    label: str

    config: CompReviewConfig

    # users who have been granted access to this comp review
    shareAccess: typing.List[ShareAccess]

class OptionalCompReview(TypedDict, total=False):
    # Whether the compensation review has been approved by the final approvers
    status: str

    # count of reviewers in the comp review
    reviewerCount: int

    # count of reviews that have been submitted and approved
    submittedCount: int

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class CompReview(RequiredCompReview, OptionalCompReview):
    pass
