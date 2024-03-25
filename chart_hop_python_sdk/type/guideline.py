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

from chart_hop_python_sdk.type.basis_field_matrix import BasisFieldMatrix
from chart_hop_python_sdk.type.money_range import MoneyRange
from chart_hop_python_sdk.type.value_range import ValueRange

class RequiredGuideline(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # comp review id
    compReviewId: str

    # guideline name
    label: str

    # the field the guideline applies to
    appliedField: str

    # the field the guideline is calculated from
    sourceField: str

    # how does the guideline calculate the target value? e.g. is there a range (min/max) or only a target
    calculationType: str

    # how does the guideline indicate deviations from the target amount
    flagMode: str

    # whether or not the target values from the guidelines are pre-populated in the given columns
    enablePopulateValue: bool

    # how an individual guideline value itself is calculated, e.g. percentage of the appliedField, fixed amount, or custom CQL
    basisType: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalGuideline(TypedDict, total=False):
    # the budget pool the guideline is allocated from
    budgetPoolId: str

    # CQL filter to determine which employees the guideline applies to
    participantsExpr: str

    # the threshold (percent) against which deviations from the guideline are flagged
    flagDeviationThreshold: typing.Union[int, float]

    # if basisType.CUSTOM, the custom CQL expression used to generate the guideline value
    basisExpr: str

    basisFieldMatrix: BasisFieldMatrix

    fixedAmountRange: MoneyRange

    fixedValueRange: ValueRange

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class Guideline(RequiredGuideline, OptionalGuideline):
    pass
