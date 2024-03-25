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

from chart_hop_python_sdk.pydantic.approval_request_comp_review_response import ApprovalRequestCompReviewResponse
from chart_hop_python_sdk.pydantic.comp_review_workbook_column import CompReviewWorkbookColumn
from chart_hop_python_sdk.pydantic.in_cycle_view_features import InCycleViewFeatures
from chart_hop_python_sdk.pydantic.in_cycle_view_response_collaborating_with_job_ids import InCycleViewResponseCollaboratingWithJobIds
from chart_hop_python_sdk.pydantic.in_cycle_view_response_error import InCycleViewResponseError
from chart_hop_python_sdk.pydantic.in_cycle_view_response_parent_reviews_map import InCycleViewResponseParentReviewsMap
from chart_hop_python_sdk.pydantic.in_cycle_view_response_scenario_map import InCycleViewResponseScenarioMap

class InCycleViewResponse(BaseModel):
    reviews: typing.Optional[typing.List[ApprovalRequestCompReviewResponse]] = Field(None, alias='reviews')

    proposal: typing.Optional[ApprovalRequestCompReviewResponse] = Field(None, alias='proposal')

    scenario_map: typing.Optional[InCycleViewResponseScenarioMap] = Field(None, alias='scenarioMap')

    parent_reviews_map: typing.Optional[InCycleViewResponseParentReviewsMap] = Field(None, alias='parentReviewsMap')

    collaborating_with_job_ids: typing.Optional[InCycleViewResponseCollaboratingWithJobIds] = Field(None, alias='collaboratingWithJobIds')

    visible_columns: typing.Optional[typing.List[CompReviewWorkbookColumn]] = Field(None, alias='visibleColumns')

    error: typing.Optional[InCycleViewResponseError] = Field(None, alias='error')

    features: typing.Optional[InCycleViewFeatures] = Field(None, alias='features')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
