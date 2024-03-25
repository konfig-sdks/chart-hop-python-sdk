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

from chart_hop_python_sdk.pydantic.comp_review_budgets import CompReviewBudgets
from chart_hop_python_sdk.pydantic.comp_review_collaborators import CompReviewCollaborators
from chart_hop_python_sdk.pydantic.comp_review_config_reassignments import CompReviewConfigReassignments
from chart_hop_python_sdk.pydantic.comp_review_eligible_employees import CompReviewEligibleEmployees
from chart_hop_python_sdk.pydantic.comp_review_key_dates import CompReviewKeyDates
from chart_hop_python_sdk.pydantic.comp_review_notifications import CompReviewNotifications
from chart_hop_python_sdk.pydantic.comp_review_reviewer_workbook import CompReviewReviewerWorkbook
from chart_hop_python_sdk.pydantic.comp_review_reviewers_approvers import CompReviewReviewersApprovers

class CompReviewConfig(BaseModel):
    key_dates: CompReviewKeyDates = Field(alias='keyDates')

    eligible_employees: CompReviewEligibleEmployees = Field(alias='eligibleEmployees')

    reviewers_and_approvers: CompReviewReviewersApprovers = Field(alias='reviewersAndApprovers')

    collaborators: CompReviewCollaborators = Field(alias='collaborators')

    reviewer_workbook: CompReviewReviewerWorkbook = Field(alias='reviewerWorkbook')

    budgets: typing.Optional[CompReviewBudgets] = Field(None, alias='budgets')

    notifications: typing.Optional[CompReviewNotifications] = Field(None, alias='notifications')

    reassignments: typing.Optional[CompReviewConfigReassignments] = Field(None, alias='reassignments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
