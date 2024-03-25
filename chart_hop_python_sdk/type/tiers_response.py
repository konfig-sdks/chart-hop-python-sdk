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

from chart_hop_python_sdk.type.tiers_response_final_approvers import TiersResponseFinalApprovers
from chart_hop_python_sdk.type.tiers_response_reviews import TiersResponseReviews

class RequiredTiersResponse(TypedDict):
    reviews: TiersResponseReviews

    finalApprovers: TiersResponseFinalApprovers

class OptionalTiersResponse(TypedDict, total=False):
    pass

class TiersResponse(RequiredTiersResponse, OptionalTiersResponse):
    pass
