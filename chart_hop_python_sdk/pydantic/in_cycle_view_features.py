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


class InCycleViewFeatures(BaseModel):
    is_final_approver: bool = Field(alias='isFinalApprover')

    is_proposer: bool = Field(alias='isProposer')

    is_approver: bool = Field(alias='isApprover')

    is_owner: bool = Field(alias='isOwner')

    is_collaborator: bool = Field(alias='isCollaborator')

    is_root: typing.Optional[bool] = Field(None, alias='isRoot')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
