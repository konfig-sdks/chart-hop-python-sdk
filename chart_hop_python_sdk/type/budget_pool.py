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
from chart_hop_python_sdk.type.budget_pool_fixed_budget_map import BudgetPoolFixedBudgetMap
from chart_hop_python_sdk.type.money import Money

class RequiredBudgetPool(TypedDict):
    # globally unique id
    id: str

    # parent organization id (empty if built-in)
    orgId: str

    # the ID of the comp review this budget is for
    compReviewId: str

    # unique label
    label: str

    # the field this budget pool applies to
    appliedField: str

    # the field this budget pool is calculated from
    sourceField: str

    # the method for calculating the amount in the budget
    basisType: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalBudgetPool(TypedDict, total=False):
    # expression that determines if a particular job is included in this budget pool
    participantsExpr: str

    fixedAmount: Money

    # a fixed amount for the budget (used with basisType=FIXED || basisType=PERCENTAGE)
    fixedValue: typing.Union[int, float]

    basisFieldMatrix: BasisFieldMatrix

    fixedBudgetMap: BudgetPoolFixedBudgetMap

    # expression that calculates how much each job contributes to the budget (used with basisType=CUSTOM)
    basisExpr: str

    # Default currency used when calculating budget pool, falls back to org primary currency if not set
    defaultCurrency: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class BudgetPool(RequiredBudgetPool, OptionalBudgetPool):
    pass
