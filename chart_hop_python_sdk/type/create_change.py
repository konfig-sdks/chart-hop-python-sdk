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

from chart_hop_python_sdk.type.job_update import JobUpdate
from chart_hop_python_sdk.type.partial_job import PartialJob

class RequiredCreateChange(TypedDict):
    pass

class OptionalCreateChange(TypedDict, total=False):
    # job id
    jobId: str

    # parent organization id
    orgId: str

    # scenario that this change belongs to
    scenarioId: str

    # the id of the person involved, or empty if no person attached to job
    personId: str

    # for MOVE changes, the id of the job moving from; for RELATE changes, the id of the other job
    otherJobId: str

    # type of change
    type: str

    # date of change
    date: date

    # for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change
    announceDate: date

    # for DEPART changes, the type of departure
    departType: str

    # for DEPART changes, whether the departure is regrettable
    departRegret: str

    # the reason of the change
    reason: str

    # if it's a promotion or a demotion
    promotionType: str

    job: PartialJob

    update: JobUpdate

    # note on the change
    note: str

class CreateChange(RequiredCreateChange, OptionalCreateChange):
    pass
