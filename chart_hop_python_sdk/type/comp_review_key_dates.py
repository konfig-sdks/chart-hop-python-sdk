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


class RequiredCompReviewKeyDates(TypedDict):
    # Date on which the comp review cycle begins
    cycleBeginDate: date

    # Date by which all levels should be submitted for approval
    levelsSubmitByDate: date

    # Date by which final approval/sign-off will be completed, this is the baseline primary effective date for the comp review
    finalApprovalDate: date

class OptionalCompReviewKeyDates(TypedDict, total=False):
    # Date on which payroll updates become effective
    payrollEffectiveDate: date

    # A custom date to use for the primary data structure
    customEffectiveDate: date

    # Whether to skip approval stages forward after the submit date
    isSkipAfterSubmitOverdue: bool

    # Whether to skip approval stages forward after the submit date
    skippedAt: int

    # whether the default config has been modified
    isEdited: bool

class CompReviewKeyDates(RequiredCompReviewKeyDates, OptionalCompReviewKeyDates):
    pass
