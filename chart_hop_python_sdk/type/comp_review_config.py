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

from chart_hop_python_sdk.type.comp_review_budgets import CompReviewBudgets
from chart_hop_python_sdk.type.comp_review_collaborators import CompReviewCollaborators
from chart_hop_python_sdk.type.comp_review_config_reassignments import CompReviewConfigReassignments
from chart_hop_python_sdk.type.comp_review_eligible_employees import CompReviewEligibleEmployees
from chart_hop_python_sdk.type.comp_review_key_dates import CompReviewKeyDates
from chart_hop_python_sdk.type.comp_review_notifications import CompReviewNotifications
from chart_hop_python_sdk.type.comp_review_reviewer_workbook import CompReviewReviewerWorkbook
from chart_hop_python_sdk.type.comp_review_reviewers_approvers import CompReviewReviewersApprovers

class RequiredCompReviewConfig(TypedDict):
    keyDates: CompReviewKeyDates

    eligibleEmployees: CompReviewEligibleEmployees

    reviewersAndApprovers: CompReviewReviewersApprovers

    collaborators: CompReviewCollaborators

    reviewerWorkbook: CompReviewReviewerWorkbook

class OptionalCompReviewConfig(TypedDict, total=False):
    budgets: CompReviewBudgets

    notifications: CompReviewNotifications

    reassignments: CompReviewConfigReassignments

class CompReviewConfig(RequiredCompReviewConfig, OptionalCompReviewConfig):
    pass
