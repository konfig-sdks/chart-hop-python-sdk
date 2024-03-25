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

from chart_hop_python_sdk.pydantic.comp_review_eligible_employees_exclude_group_ids import CompReviewEligibleEmployeesExcludeGroupIds
from chart_hop_python_sdk.pydantic.comp_review_eligible_employees_excluded_employment_statuses import CompReviewEligibleEmployeesExcludedEmploymentStatuses
from chart_hop_python_sdk.pydantic.comp_review_eligible_employees_individual_exclusions import CompReviewEligibleEmployeesIndividualExclusions
from chart_hop_python_sdk.pydantic.comp_review_eligible_employees_individual_inclusions import CompReviewEligibleEmployeesIndividualInclusions

class CompReviewEligibleEmployees(BaseModel):
    # Defines who is ineligible for this cycle
    ineligibility_type: Literal["NONE", "DEPARTMENT", "DIVISION", "LOCATION", "CUSTOM"] = Field(alias='ineligibilityType')

    excluded_employment_statuses: typing.Optional[CompReviewEligibleEmployeesExcludedEmploymentStatuses] = Field(None, alias='excludedEmploymentStatuses')

    exclude_group_ids: typing.Optional[CompReviewEligibleEmployeesExcludeGroupIds] = Field(None, alias='excludeGroupIds')

    # The filter to apply when custom ineligibility rules is selected
    filter: typing.Optional[str] = Field(None, alias='filter')

    # The cutoff date of last raise if specified
    last_raise_date: typing.Optional[date] = Field(None, alias='lastRaiseDate')

    # The cutoff start date if specified
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    individual_exclusions: typing.Optional[CompReviewEligibleEmployeesIndividualExclusions] = Field(None, alias='individualExclusions')

    individual_inclusions: typing.Optional[CompReviewEligibleEmployeesIndividualInclusions] = Field(None, alias='individualInclusions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
