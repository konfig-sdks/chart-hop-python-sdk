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

class CreateChange(BaseModel):
    # job id
    job_id: typing.Optional[str] = Field(None, alias='jobId')

    # parent organization id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # scenario that this change belongs to
    scenario_id: typing.Optional[str] = Field(None, alias='scenarioId')

    # the id of the person involved, or empty if no person attached to job
    person_id: typing.Optional[str] = Field(None, alias='personId')

    # for MOVE changes, the id of the job moving from; for RELATE changes, the id of the other job
    other_job_id: typing.Optional[str] = Field(None, alias='otherJobId')

    # type of change
    type: typing.Optional[Literal["HIRE", "DEPART", "MOVE", "UPCOMING", "CREATE", "UPDATE", "DATA", "DELETE", "RELATE", "BACKFILL"]] = Field(None, alias='type')

    # date of change
    date: typing.Optional[date] = Field(None, alias='date')

    # for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change
    announce_date: typing.Optional[date] = Field(None, alias='announceDate')

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

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
