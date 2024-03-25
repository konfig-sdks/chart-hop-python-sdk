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

from chart_hop_python_sdk.pydantic.job_update import JobUpdate
from chart_hop_python_sdk.pydantic.partial_job import PartialJob

class UpdateChange(BaseModel):
    # date of change
    date: typing.Optional[date] = Field(None, alias='date')

    # for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change
    announce_date: typing.Optional[date] = Field(None, alias='announceDate')

    # whether the change is active or not
    status: typing.Optional[Literal["ACTIVE", "STRUCK", "CONFLICT", "INACTIVE", "PROPOSED"]] = Field(None, alias='status')

    # for DEPART changes, the type of departure
    depart_type: typing.Optional[Literal["VOLUNTARY", "INVOLUNTARY"]] = Field(None, alias='departType')

    # for DEPART changes, whether the departure is regrettable
    depart_regret: typing.Optional[Literal["REGRET", "NONREGRET"]] = Field(None, alias='departRegret')

    # the reason of the change
    reason: typing.Optional[str] = Field(None, alias='reason')

    # if it's a promotion or a demotion
    promotion_type: typing.Optional[Literal["PROMOTION", "DEMOTION", "NONE"]] = Field(None, alias='promotionType')

    job: typing.Optional[PartialJob] = Field(None, alias='job')

    update: typing.Optional[JobUpdate] = Field(None, alias='update')

    # note on the change
    note: typing.Optional[str] = Field(None, alias='note')

    # approval/rejection note
    approval_note: typing.Optional[str] = Field(None, alias='approvalNote')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
