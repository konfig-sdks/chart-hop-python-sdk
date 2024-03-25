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


class ApprovalGroupApprover(BaseModel):
    # A job ID that is part of the group
    job_id: str = Field(alias='jobId')

    # The status of the approver
    status: Literal["PENDING", "APPROVED", "REJECTED"] = Field(alias='status')

    # Last comment of the approver
    comment_id: typing.Optional[str] = Field(None, alias='commentId')

    # Last comment associated with a reassignment
    reassign_comment_id: typing.Optional[str] = Field(None, alias='reassignCommentId')

    # Whether approver is a fallback
    is_fallback: typing.Optional[bool] = Field(None, alias='isFallback')

    # What jobId approver is a fallback for
    fallback_for: typing.Optional[str] = Field(None, alias='fallbackFor')

    # The date the status was updated last
    update_at: typing.Optional[int] = Field(None, alias='updateAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
