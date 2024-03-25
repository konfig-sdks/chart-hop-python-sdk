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

from chart_hop_python_sdk.pydantic.approval_group import ApprovalGroup

class ApprovalChainStage(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # parent approval chain id
    approval_chain_id: str = Field(alias='approvalChainId')

    # determines which stage becomes active when a rejection event happens
    reject_behavior: Literal["BACK_TO_BEGINNING", "PREVIOUS_PHASE"] = Field(alias='rejectBehavior')

    # status of the stage
    status: Literal["CANCELED", "REJECTED", "PENDING", "ACTIVE", "REVIEWED", "APPROVED", "SKIPPED", "SUBMITTED"] = Field(alias='status')

    # requires a comment on an approval event
    approval_comment_required: bool = Field(alias='approvalCommentRequired')

    # requires a comment on an rejection event
    rejection_comment_required: bool = Field(alias='rejectionCommentRequired')

    # order of stage in approval chain
    order: int = Field(alias='order')

    # list of groups that are involved in this approval stage
    groups: typing.List[ApprovalGroup] = Field(alias='groups')

    # optional custom expression to determine stage inclusion behavior
    inclusion_expression: typing.Optional[str] = Field(None, alias='inclusionExpression')

    # determines whether stage is conditional based on an expression
    inclusion_behavior: typing.Optional[Literal["ONLY_INCLUDE_IF", "EXCLUDE_IF"]] = Field(None, alias='inclusionBehavior')

    # optional custom expression to determine approval request tree
    expand_expression: typing.Optional[str] = Field(None, alias='expandExpression')

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
