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

class ApprovalRequestCompReviewResponse(BaseModel):
    id: str = Field(alias='id')

    status: Literal["CANCELED", "REJECTED", "PENDING", "ACTIVE", "REVIEWED", "APPROVED", "SKIPPED", "SUBMITTED"] = Field(alias='status')

    entity_type: Literal["COMP_REVIEW", "SCENARIO", "TIMEOFF"] = Field(alias='entityType')

    entity_id: str = Field(alias='entityId')

    approval_chain_id: str = Field(alias='approvalChainId')

    stage_overrides: typing.List[ApprovalChainStageOverride] = Field(alias='stageOverrides')

    parent_status: typing.Optional[Literal["CANCELED", "REJECTED", "PENDING", "ACTIVE", "REVIEWED", "APPROVED", "SKIPPED", "SUBMITTED"]] = Field(None, alias='parentStatus')

    is_fully_submitted: typing.Optional[bool] = Field(None, alias='isFullySubmitted')

    create_id: typing.Optional[str] = Field(None, alias='createId')

    create_at: typing.Optional[int] = Field(None, alias='createAt')

    update_id: typing.Optional[str] = Field(None, alias='updateId')

    update_at: typing.Optional[int] = Field(None, alias='updateAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
