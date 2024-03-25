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

class RequiredUpdateChange(TypedDict):
    pass

class OptionalUpdateChange(TypedDict, total=False):
    # date of change
    date: date

    # for HIRE and DEPART changes, the announce date, if the announce date is different from the date of change
    announceDate: date

    # whether the change is active or not
    status: str

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

    # approval/rejection note
    approvalNote: str

class UpdateChange(RequiredUpdateChange, OptionalUpdateChange):
    pass
