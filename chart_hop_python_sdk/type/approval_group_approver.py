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


class RequiredApprovalGroupApprover(TypedDict):
    # A job ID that is part of the group
    jobId: str

    # The status of the approver
    status: str

class OptionalApprovalGroupApprover(TypedDict, total=False):
    # Last comment of the approver
    commentId: str

    # Last comment associated with a reassignment
    reassignCommentId: str

    # Whether approver is a fallback
    isFallback: bool

    # What jobId approver is a fallback for
    fallbackFor: str

    # The date the status was updated last
    updateAt: int

class ApprovalGroupApprover(RequiredApprovalGroupApprover, OptionalApprovalGroupApprover):
    pass
