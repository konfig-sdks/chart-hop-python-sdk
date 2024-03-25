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

from chart_hop_python_sdk.type.approval_chain_stage_override import ApprovalChainStageOverride

class RequiredApprovalRequestCompReviewResponse(TypedDict):
    id: str

    status: str

    entityType: str

    entityId: str

    approvalChainId: str

    stageOverrides: typing.List[ApprovalChainStageOverride]

class OptionalApprovalRequestCompReviewResponse(TypedDict, total=False):
    parentStatus: str

    isFullySubmitted: bool

    createId: str

    createAt: int

    updateId: str

    updateAt: int

class ApprovalRequestCompReviewResponse(RequiredApprovalRequestCompReviewResponse, OptionalApprovalRequestCompReviewResponse):
    pass
