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


class EvaluateExpressionRequest(BaseModel):
    expr: str = Field(alias='expr')

    entity_type: Literal["ACTION", "AGREEMENT", "APP", "APP_CONFIG", "APPROVAL_CHAIN", "APPROVAL_CHAIN_STAGE", "APPROVAL_REQUEST", "ASSESSMENT", "BUDGET_POOL", "BUNDLE", "CATEGORY", "CATEGORY_SORT", "CHANGE", "COMMENT", "COMP_BAND", "COMP_REVIEW", "CONTENT", "CUSTOMER", "DATA_VIEW", "EXCHANGE_RATE", "EMAIL_TEMPLATE", "FIELD", "FILE", "FORM", "FORM_DRAFT", "FORM_RESPONSE", "GEOCODE", "GROUP", "GUIDELINE", "JOB", "JOB_LEVEL", "MEDIA", "MESSAGE", "MULTIPLIER", "ORG", "ORG_CONFIG", "PERSON", "PROFILE_TAB", "POLICY", "POSITION", "PROCESS", "PRODUCT", "QUERY_TOKEN", "QUESTION", "REPORT", "REPORT_CHART", "ROLE", "SCENARIO", "STOCK_PRICE", "TABLE", "TABLE_ROW", "TASK_CONFIG", "TEMPLATE", "TASK", "TOKEN", "TIMEOFF", "TRACKED_GROUP", "USER"] = Field(alias='entityType')

    entity_id: str = Field(alias='entityId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
