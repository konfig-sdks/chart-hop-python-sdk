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

from chart_hop_python_sdk.pydantic.approval_chain_approval_notifier_user_ids import ApprovalChainApprovalNotifierUserIds

class ApprovalChain(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # human-readable name of approval chain
    name: str = Field(alias='name')

    approval_notifier_user_ids: ApprovalChainApprovalNotifierUserIds = Field(alias='approvalNotifierUserIds')

    # entity id
    entity_id: typing.Optional[str] = Field(None, alias='entityId')

    # entity type
    entity_type: typing.Optional[Literal["COMP_REVIEW", "SCENARIO", "TIMEOFF"]] = Field(None, alias='entityType')

    # isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)
    is_preview: typing.Optional[bool] = Field(None, alias='isPreview')

    # the jobId of the fallback approver
    fallback_approver_job_id: typing.Optional[str] = Field(None, alias='fallbackApproverJobId')

    # most recent error for fallback approver
    fallback_approver_job_error: typing.Optional[str] = Field(None, alias='fallbackApproverJobError')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
