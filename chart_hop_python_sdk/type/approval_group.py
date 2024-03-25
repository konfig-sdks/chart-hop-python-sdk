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

from chart_hop_python_sdk.type.approval_group_approver import ApprovalGroupApprover

class RequiredApprovalGroup(TypedDict):
    # What type of group this is
    type: str

    # approvers that make up the group
    approvers: typing.List[ApprovalGroupApprover]

class OptionalApprovalGroup(TypedDict, total=False):
    # globally unique id
    groupId: str

    # optional custom expression to determine approval request tree
    expandExpression: str

class ApprovalGroup(RequiredApprovalGroup, OptionalApprovalGroup):
    pass
