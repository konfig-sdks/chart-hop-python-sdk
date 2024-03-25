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

from chart_hop_python_sdk.pydantic.basis_field_matrix import BasisFieldMatrix
from chart_hop_python_sdk.pydantic.create_budget_pool_fixed_budget_map import CreateBudgetPoolFixedBudgetMap
from chart_hop_python_sdk.pydantic.money import Money

class CreateBudgetPool(BaseModel):
    # the ID of the comp review this budget is for
    comp_review_id: str = Field(alias='compReviewId')

    # unique label
    label: str = Field(alias='label')

    # the field this budget pool applies to
    applied_field: str = Field(alias='appliedField')

    # the field this budget pool is calculated from
    source_field: str = Field(alias='sourceField')

    # the method for calculating the amount in the budget
    basis_type: Literal["CUSTOM", "FIXED", "CUSTOM_FIXED", "PERCENTAGE", "CUSTOM_PERCENTAGE"] = Field(alias='basisType')

    # expression that determines if a particular job is included in this budget pool
    participants_expr: typing.Optional[str] = Field(None, alias='participantsExpr')

    fixed_amount: typing.Optional[Money] = Field(None, alias='fixedAmount')

    # a fixed amount for the budget (used with basisType=FIXED || basisType=PERCENTAGE)
    fixed_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='fixedValue')

    basis_field_matrix: typing.Optional[BasisFieldMatrix] = Field(None, alias='basisFieldMatrix')

    fixed_budget_map: typing.Optional[CreateBudgetPoolFixedBudgetMap] = Field(None, alias='fixedBudgetMap')

    # expression that calculates how much each job contributes to the budget (used with basisType=CUSTOM)
    basis_expr: typing.Optional[str] = Field(None, alias='basisExpr')

    # Default currency used when calculating budget pool, falls back to org primary currency if not set
    default_currency: typing.Optional[str] = Field(None, alias='defaultCurrency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
