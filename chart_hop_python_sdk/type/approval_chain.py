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

from chart_hop_python_sdk.type.approval_chain_approval_notifier_user_ids import ApprovalChainApprovalNotifierUserIds

class RequiredApprovalChain(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable name of approval chain
    name: str

    approvalNotifierUserIds: ApprovalChainApprovalNotifierUserIds

class OptionalApprovalChain(TypedDict, total=False):
    # entity id
    entityId: str

    # entity type
    entityType: str

    # isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)
    isPreview: bool

    # the jobId of the fallback approver
    fallbackApproverJobId: str

    # most recent error for fallback approver
    fallbackApproverJobError: str

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

class ApprovalChain(RequiredApprovalChain, OptionalApprovalChain):
    pass
