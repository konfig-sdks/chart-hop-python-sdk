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

from chart_hop_python_sdk.pydantic.approval_group_approver import ApprovalGroupApprover

class ApprovalGroup(BaseModel):
    # What type of group this is
    type: Literal["REVIEWER", "COLLABORATOR", "FINAL_APPROVER"] = Field(alias='type')

    # approvers that make up the group
    approvers: typing.List[ApprovalGroupApprover] = Field(alias='approvers')

    # globally unique id
    group_id: typing.Optional[str] = Field(None, alias='groupId')

    # optional custom expression to determine approval request tree
    expand_expression: typing.Optional[str] = Field(None, alias='expandExpression')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
