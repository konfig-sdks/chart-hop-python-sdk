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


class CompReviewKeyDates(BaseModel):
    # Date on which the comp review cycle begins
    cycle_begin_date: date = Field(alias='cycleBeginDate')

    # Date by which all levels should be submitted for approval
    levels_submit_by_date: date = Field(alias='levelsSubmitByDate')

    # Date by which final approval/sign-off will be completed, this is the baseline primary effective date for the comp review
    final_approval_date: date = Field(alias='finalApprovalDate')

    # Date on which payroll updates become effective
    payroll_effective_date: typing.Optional[date] = Field(None, alias='payrollEffectiveDate')

    # A custom date to use for the primary data structure
    custom_effective_date: typing.Optional[date] = Field(None, alias='customEffectiveDate')

    # Whether to skip approval stages forward after the submit date
    is_skip_after_submit_overdue: typing.Optional[bool] = Field(None, alias='isSkipAfterSubmitOverdue')

    # Whether to skip approval stages forward after the submit date
    skipped_at: typing.Optional[int] = Field(None, alias='skippedAt')

    # whether the default config has been modified
    is_edited: typing.Optional[bool] = Field(None, alias='isEdited')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
