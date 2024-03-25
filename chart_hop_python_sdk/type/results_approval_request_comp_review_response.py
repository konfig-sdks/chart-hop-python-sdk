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

from chart_hop_python_sdk.type.approval_request_comp_review_response import ApprovalRequestCompReviewResponse

class RequiredResultsApprovalRequestCompReviewResponse(TypedDict):
    data: typing.List[ApprovalRequestCompReviewResponse]

class OptionalResultsApprovalRequestCompReviewResponse(TypedDict, total=False):
    next: str

class ResultsApprovalRequestCompReviewResponse(RequiredResultsApprovalRequestCompReviewResponse, OptionalResultsApprovalRequestCompReviewResponse):
    pass
