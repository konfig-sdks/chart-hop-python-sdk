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

from chart_hop_python_sdk.type.approval_chain_stage_override import ApprovalChainStageOverride

class RequiredApprovalRequest(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # entity id
    entityId: str

    # entity type
    entityType: str

    # parent approval chain id
    approvalChainId: str

    # list of configuration fields
    stageOverrides: typing.List[ApprovalChainStageOverride]

class OptionalApprovalRequest(TypedDict, total=False):
    # comp review id
    compReviewId: str

    # the user who requested the approval
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

class ApprovalRequest(RequiredApprovalRequest, OptionalApprovalRequest):
    pass
