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

from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredCreateAssessment(TypedDict):
    # human-readable label of assessment
    label: str

    # type of assessment
    type: str

class OptionalCreateAssessment(TypedDict, total=False):
    # unique slug of assessment
    slug: str

    # assessment fields (description)
    fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # users who have been granted access to this assessment
    shareAccess: typing.List[ShareAccess]

    # view sensitivity of this assessment
    sensitive: str

    # color of assessment
    color: str

    # Date this assessment begins. In the context of REVIEW goals, the date the review cycle begins.
    startDate: date

    # Date this assessment ends, or is completed. In the context of REVIEW assessment, the date the review cycle ends.
    endDate: date

    # status of this assessment - DRAFT, ACTIVE, DONE
    status: str

    # timestamp when the status of this assessment was set to done
    doneAt: str

    # number of tasks associated with this assessment
    taskCount: int

    # number of tasks associated with this assessment that are done
    taskDoneCount: int

    # number of people included in this assessment
    peopleIncludedCount: int

    # Query for which people/jobs can be included in the review.
    query: str

class CreateAssessment(RequiredCreateAssessment, OptionalCreateAssessment):
    pass
