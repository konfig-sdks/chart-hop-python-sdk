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

from chart_hop_python_sdk.pydantic.create_approval_chain_approval_notifier_user_ids import CreateApprovalChainApprovalNotifierUserIds

class CreateApprovalChain(BaseModel):
    # human-readable name of approval chain
    name: str = Field(alias='name')

    # isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)
    is_preview: bool = Field(alias='isPreview')

    approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds = Field(alias='approvalNotifierUserIds')

    # entity id
    entity_id: typing.Optional[str] = Field(None, alias='entityId')

    # entity type
    entity_type: typing.Optional[Literal["COMP_REVIEW", "SCENARIO", "TIMEOFF"]] = Field(None, alias='entityType')

    # the jobId of the fallback approver
    fallback_approver_job_id: typing.Optional[str] = Field(None, alias='fallbackApproverJobId')

    # most recent error for fallback approver
    fallback_approver_job_error: typing.Optional[str] = Field(None, alias='fallbackApproverJobError')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
