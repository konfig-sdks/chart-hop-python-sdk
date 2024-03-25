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

class RequiredApprovalRequestScenarioResponse(TypedDict):
    id: str

    isComplete: bool

    stageOverrides: typing.List[ApprovalChainStageOverride]

    isApprovalCommentRequiredForActiveStage: bool

    isRejectionCommentRequiredForActiveStage: bool

    approvalChainId: str

    scenarioId: str

    createId: str

    createAt: int

    updateId: str

    updateAt: int

class OptionalApprovalRequestScenarioResponse(TypedDict, total=False):
    activeStage: ApprovalChainStageOverride

    proposerStage: ApprovalChainStageOverride

    nextReviewerStage: ApprovalChainStageOverride

    rejectedStage: ApprovalChainStageOverride

    deleteId: str

    deleteAt: int

class ApprovalRequestScenarioResponse(RequiredApprovalRequestScenarioResponse, OptionalApprovalRequestScenarioResponse):
    pass
