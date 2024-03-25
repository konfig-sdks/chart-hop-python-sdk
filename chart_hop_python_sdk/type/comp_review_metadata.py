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


class RequiredCompReviewMetadata(TypedDict):
    # comp review id
    compReviewId: str

    # parent organization id (empty if built-in)
    orgId: str

    # count of employees eligible for the comp review
    eligibleEmployees: int

    # filter to view eligible employees on the datasheet
    eligibleEmployeesFilter: str

    # count of employees ineligible for the comp review
    ineligibleEmployees: int

    # filter to view ineligible employees on the datasheet
    ineligibleEmployeesFilter: str

    # count of final approvers
    approvers: int

    # count of reviewers in the comp review
    reviewers: int

    # count of collaborators in the comp review
    collaborators: int

class OptionalCompReviewMetadata(TypedDict, total=False):
    pass

class CompReviewMetadata(RequiredCompReviewMetadata, OptionalCompReviewMetadata):
    pass
