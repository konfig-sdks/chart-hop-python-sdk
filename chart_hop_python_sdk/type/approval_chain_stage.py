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

from chart_hop_python_sdk.type.approval_group import ApprovalGroup

class RequiredApprovalChainStage(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # parent approval chain id
    approvalChainId: str

    # determines which stage becomes active when a rejection event happens
    rejectBehavior: str

    # status of the stage
    status: str

    # requires a comment on an approval event
    approvalCommentRequired: bool

    # requires a comment on an rejection event
    rejectionCommentRequired: bool

    # order of stage in approval chain
    order: int

    # list of groups that are involved in this approval stage
    groups: typing.List[ApprovalGroup]

class OptionalApprovalChainStage(TypedDict, total=False):
    # optional custom expression to determine stage inclusion behavior
    inclusionExpression: str

    # determines whether stage is conditional based on an expression
    inclusionBehavior: str

    # optional custom expression to determine approval request tree
    expandExpression: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class ApprovalChainStage(RequiredApprovalChainStage, OptionalApprovalChainStage):
    pass
