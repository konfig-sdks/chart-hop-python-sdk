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

class ApprovalChainStageOverride(BaseModel):
    # unique id for stage
    stage_override_id: str = Field(alias='stageOverrideId')

    # parent approval chain stage id
    approval_chain_stage_id: str = Field(alias='approvalChainStageId')

    # status of the stage
    status: Literal["CANCELED", "REJECTED", "PENDING", "ACTIVE", "REVIEWED", "APPROVED", "SKIPPED", "SUBMITTED"] = Field(alias='status')

    # order of the stage
    order: int = Field(alias='order')

    # approval group override
    groups: typing.Optional[typing.List[ApprovalGroup]] = Field(None, alias='groups')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
