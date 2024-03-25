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

class UpdateApprovalChainStage(BaseModel):
    # optional custom expression to determine stage inclusion behavior
    inclusion_expression: typing.Optional[str] = Field(None, alias='inclusionExpression')

    # determines whether stage is conditional based on an expression
    inclusion_behavior: typing.Optional[Literal["ONLY_INCLUDE_IF", "EXCLUDE_IF"]] = Field(None, alias='inclusionBehavior')

    # optional custom expression to determine approval request tree
    expand_expression: typing.Optional[str] = Field(None, alias='expandExpression')

    # determines which stage becomes active when a rejection event happens
    reject_behavior: typing.Optional[Literal["BACK_TO_BEGINNING", "PREVIOUS_PHASE"]] = Field(None, alias='rejectBehavior')

    # status of the stage
    status: typing.Optional[Literal["CANCELED", "REJECTED", "PENDING", "ACTIVE", "REVIEWED", "APPROVED", "SKIPPED", "SUBMITTED"]] = Field(None, alias='status')

    # requires a comment on an approval event
    approval_comment_required: typing.Optional[bool] = Field(None, alias='approvalCommentRequired')

    # requires a comment on an rejection event
    rejection_comment_required: typing.Optional[bool] = Field(None, alias='rejectionCommentRequired')

    # order of stage in approval chain
    order: typing.Optional[int] = Field(None, alias='order')

    # list of groups that are involved in this approval stage
    groups: typing.Optional[typing.List[ApprovalGroup]] = Field(None, alias='groups')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
