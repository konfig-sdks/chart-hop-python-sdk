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

from chart_hop_python_sdk.type.create_approval_chain_approval_notifier_user_ids import CreateApprovalChainApprovalNotifierUserIds

class RequiredCreateApprovalChain(TypedDict):
    # human-readable name of approval chain
    name: str

    # isPreview specifies that this is a preview for implementations that use it (e.g. Compensation Reviews)
    isPreview: bool

    approvalNotifierUserIds: CreateApprovalChainApprovalNotifierUserIds

class OptionalCreateApprovalChain(TypedDict, total=False):
    # entity id
    entityId: str

    # entity type
    entityType: str

    # the jobId of the fallback approver
    fallbackApproverJobId: str

    # most recent error for fallback approver
    fallbackApproverJobError: str

class CreateApprovalChain(RequiredCreateApprovalChain, OptionalCreateApprovalChain):
    pass
