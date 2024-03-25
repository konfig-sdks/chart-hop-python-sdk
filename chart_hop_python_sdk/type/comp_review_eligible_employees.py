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

from chart_hop_python_sdk.type.comp_review_eligible_employees_exclude_group_ids import CompReviewEligibleEmployeesExcludeGroupIds
from chart_hop_python_sdk.type.comp_review_eligible_employees_excluded_employment_statuses import CompReviewEligibleEmployeesExcludedEmploymentStatuses
from chart_hop_python_sdk.type.comp_review_eligible_employees_individual_exclusions import CompReviewEligibleEmployeesIndividualExclusions
from chart_hop_python_sdk.type.comp_review_eligible_employees_individual_inclusions import CompReviewEligibleEmployeesIndividualInclusions

class RequiredCompReviewEligibleEmployees(TypedDict):
    # Defines who is ineligible for this cycle
    ineligibilityType: str

class OptionalCompReviewEligibleEmployees(TypedDict, total=False):
    excludedEmploymentStatuses: CompReviewEligibleEmployeesExcludedEmploymentStatuses

    excludeGroupIds: CompReviewEligibleEmployeesExcludeGroupIds

    # The filter to apply when custom ineligibility rules is selected
    filter: str

    # The cutoff date of last raise if specified
    lastRaiseDate: date

    # The cutoff start date if specified
    startDate: date

    individualExclusions: CompReviewEligibleEmployeesIndividualExclusions

    individualInclusions: CompReviewEligibleEmployeesIndividualInclusions

class CompReviewEligibleEmployees(RequiredCompReviewEligibleEmployees, OptionalCompReviewEligibleEmployees):
    pass
