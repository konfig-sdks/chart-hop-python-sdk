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

class RequiredApprovalChainStageOverride(TypedDict):
    # unique id for stage
    stageOverrideId: str

    # parent approval chain stage id
    approvalChainStageId: str

    # status of the stage
    status: str

    # order of the stage
    order: int

class OptionalApprovalChainStageOverride(TypedDict, total=False):
    # approval group override
    groups: typing.List[ApprovalGroup]

class ApprovalChainStageOverride(RequiredApprovalChainStageOverride, OptionalApprovalChainStageOverride):
    pass
