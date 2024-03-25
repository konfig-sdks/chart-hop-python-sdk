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

from chart_hop_python_sdk.type.approval_request_comp_review_response import ApprovalRequestCompReviewResponse
from chart_hop_python_sdk.type.comp_review_workbook_column import CompReviewWorkbookColumn
from chart_hop_python_sdk.type.in_cycle_view_features import InCycleViewFeatures
from chart_hop_python_sdk.type.in_cycle_view_response_collaborating_with_job_ids import InCycleViewResponseCollaboratingWithJobIds
from chart_hop_python_sdk.type.in_cycle_view_response_error import InCycleViewResponseError
from chart_hop_python_sdk.type.in_cycle_view_response_parent_reviews_map import InCycleViewResponseParentReviewsMap
from chart_hop_python_sdk.type.in_cycle_view_response_scenario_map import InCycleViewResponseScenarioMap

class RequiredInCycleViewResponse(TypedDict):
    pass

class OptionalInCycleViewResponse(TypedDict, total=False):
    reviews: typing.List[ApprovalRequestCompReviewResponse]

    proposal: ApprovalRequestCompReviewResponse

    scenarioMap: InCycleViewResponseScenarioMap

    parentReviewsMap: InCycleViewResponseParentReviewsMap

    collaboratingWithJobIds: InCycleViewResponseCollaboratingWithJobIds

    visibleColumns: typing.List[CompReviewWorkbookColumn]

    error: InCycleViewResponseError

    features: InCycleViewFeatures

class InCycleViewResponse(RequiredInCycleViewResponse, OptionalInCycleViewResponse):
    pass
