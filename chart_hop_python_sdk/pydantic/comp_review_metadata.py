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


class CompReviewMetadata(BaseModel):
    # comp review id
    comp_review_id: str = Field(alias='compReviewId')

    # parent organization id (empty if built-in)
    org_id: str = Field(alias='orgId')

    # count of employees eligible for the comp review
    eligible_employees: int = Field(alias='eligibleEmployees')

    # filter to view eligible employees on the datasheet
    eligible_employees_filter: str = Field(alias='eligibleEmployeesFilter')

    # count of employees ineligible for the comp review
    ineligible_employees: int = Field(alias='ineligibleEmployees')

    # filter to view ineligible employees on the datasheet
    ineligible_employees_filter: str = Field(alias='ineligibleEmployeesFilter')

    # count of final approvers
    approvers: int = Field(alias='approvers')

    # count of reviewers in the comp review
    reviewers: int = Field(alias='reviewers')

    # count of collaborators in the comp review
    collaborators: int = Field(alias='collaborators')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
