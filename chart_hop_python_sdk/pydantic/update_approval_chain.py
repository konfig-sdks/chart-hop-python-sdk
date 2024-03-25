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

from chart_hop_python_sdk.pydantic.update_approval_chain_approval_notifier_user_ids import UpdateApprovalChainApprovalNotifierUserIds

class UpdateApprovalChain(BaseModel):
    # human-readable name of approval chain
    name: typing.Optional[str] = Field(None, alias='name')

    # isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)
    is_preview: typing.Optional[bool] = Field(None, alias='isPreview')

    # the jobId of the fallback approver
    fallback_approver_job_id: typing.Optional[str] = Field(None, alias='fallbackApproverJobId')

    # most recent error for fallback approver
    fallback_approver_job_error: typing.Optional[str] = Field(None, alias='fallbackApproverJobError')

    approval_notifier_user_ids: typing.Optional[UpdateApprovalChainApprovalNotifierUserIds] = Field(None, alias='approvalNotifierUserIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
