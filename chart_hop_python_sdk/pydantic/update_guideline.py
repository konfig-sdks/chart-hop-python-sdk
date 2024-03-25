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
from chart_hop_python_sdk.pydantic.money_range import MoneyRange
from chart_hop_python_sdk.pydantic.value_range import ValueRange

class UpdateGuideline(BaseModel):
    # guideline name
    label: typing.Optional[str] = Field(None, alias='label')

    # the budget pool the guideline is allocated from
    budget_pool_id: typing.Optional[str] = Field(None, alias='budgetPoolId')

    # CQL filter to determine which employees the guideline applies to
    participants_expr: typing.Optional[str] = Field(None, alias='participantsExpr')

    # the field the guideline applies to
    applied_field: typing.Optional[str] = Field(None, alias='appliedField')

    # the field the guideline is calculated from
    source_field: typing.Optional[str] = Field(None, alias='sourceField')

    # how does the guideline calculate the target value? e.g. is there a range (min/max) or only a target
    calculation_type: typing.Optional[Literal["RANGE", "TARGET"]] = Field(None, alias='calculationType')

    # how does the guideline indicate deviations from the target amount
    flag_mode: typing.Optional[Literal["DEVIATION_THRESHOLD", "NONE"]] = Field(None, alias='flagMode')

    # the threshold (percent) against which deviations from the guideline are flagged
    flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = Field(None, alias='flagDeviationThreshold')

    # whether or not the target values from the guidelines are pre-populated in the given columns
    enable_populate_value: typing.Optional[bool] = Field(None, alias='enablePopulateValue')

    # how an individual guideline value itself is calculated, e.g. percentage of the appliedField, fixed amount, or custom CQL
    basis_type: typing.Optional[Literal["CUSTOM", "FIXED", "CUSTOM_FIXED", "PERCENTAGE", "CUSTOM_PERCENTAGE"]] = Field(None, alias='basisType')

    # if basisType.CUSTOM, the custom CQL expression used to generate the guideline value
    basis_expr: typing.Optional[str] = Field(None, alias='basisExpr')

    basis_field_matrix: typing.Optional[BasisFieldMatrix] = Field(None, alias='basisFieldMatrix')

    fixed_amount_range: typing.Optional[MoneyRange] = Field(None, alias='fixedAmountRange')

    fixed_value_range: typing.Optional[ValueRange] = Field(None, alias='fixedValueRange')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
