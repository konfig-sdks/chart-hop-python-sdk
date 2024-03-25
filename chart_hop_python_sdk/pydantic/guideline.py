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

class Guideline(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # comp review id
    comp_review_id: str = Field(alias='compReviewId')

    # guideline name
    label: str = Field(alias='label')

    # the field the guideline applies to
    applied_field: str = Field(alias='appliedField')

    # the field the guideline is calculated from
    source_field: str = Field(alias='sourceField')

    # how does the guideline calculate the target value? e.g. is there a range (min/max) or only a target
    calculation_type: Literal["RANGE", "TARGET"] = Field(alias='calculationType')

    # how does the guideline indicate deviations from the target amount
    flag_mode: Literal["DEVIATION_THRESHOLD", "NONE"] = Field(alias='flagMode')

    # whether or not the target values from the guidelines are pre-populated in the given columns
    enable_populate_value: bool = Field(alias='enablePopulateValue')

    # how an individual guideline value itself is calculated, e.g. percentage of the appliedField, fixed amount, or custom CQL
    basis_type: Literal["CUSTOM", "FIXED", "CUSTOM_FIXED", "PERCENTAGE", "CUSTOM_PERCENTAGE"] = Field(alias='basisType')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # last updated by user id
    update_id: str = Field(alias='updateId')

    # last updated timestamp
    update_at: str = Field(alias='updateAt')

    # the budget pool the guideline is allocated from
    budget_pool_id: typing.Optional[str] = Field(None, alias='budgetPoolId')

    # CQL filter to determine which employees the guideline applies to
    participants_expr: typing.Optional[str] = Field(None, alias='participantsExpr')

    # the threshold (percent) against which deviations from the guideline are flagged
    flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = Field(None, alias='flagDeviationThreshold')

    # if basisType.CUSTOM, the custom CQL expression used to generate the guideline value
    basis_expr: typing.Optional[str] = Field(None, alias='basisExpr')

    basis_field_matrix: typing.Optional[BasisFieldMatrix] = Field(None, alias='basisFieldMatrix')

    fixed_amount_range: typing.Optional[MoneyRange] = Field(None, alias='fixedAmountRange')

    fixed_value_range: typing.Optional[ValueRange] = Field(None, alias='fixedValueRange')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
