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

from chart_hop_python_sdk.pydantic.approval_chain_stage_override import ApprovalChainStageOverride

class ApprovalRequestScenarioResponse(BaseModel):
    id: str = Field(alias='id')

    is_complete: bool = Field(alias='isComplete')

    stage_overrides: typing.List[ApprovalChainStageOverride] = Field(alias='stageOverrides')

    is_approval_comment_required_for_active_stage: bool = Field(alias='isApprovalCommentRequiredForActiveStage')

    is_rejection_comment_required_for_active_stage: bool = Field(alias='isRejectionCommentRequiredForActiveStage')

    approval_chain_id: str = Field(alias='approvalChainId')

    scenario_id: str = Field(alias='scenarioId')

    create_id: str = Field(alias='createId')

    create_at: int = Field(alias='createAt')

    update_id: str = Field(alias='updateId')

    update_at: int = Field(alias='updateAt')

    active_stage: typing.Optional[ApprovalChainStageOverride] = Field(None, alias='activeStage')

    proposer_stage: typing.Optional[ApprovalChainStageOverride] = Field(None, alias='proposerStage')

    next_reviewer_stage: typing.Optional[ApprovalChainStageOverride] = Field(None, alias='nextReviewerStage')

    rejected_stage: typing.Optional[ApprovalChainStageOverride] = Field(None, alias='rejectedStage')

    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    delete_at: typing.Optional[int] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
