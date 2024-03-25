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

from chart_hop_python_sdk.type.basis_condition import BasisCondition
from chart_hop_python_sdk.type.basis_field_matrix_included_fields import BasisFieldMatrixIncludedFields

class RequiredBasisFieldMatrix(TypedDict):
    includedFields: BasisFieldMatrixIncludedFields

    conditions: typing.List[BasisCondition]

class OptionalBasisFieldMatrix(TypedDict, total=False):
    pass

class BasisFieldMatrix(RequiredBasisFieldMatrix, OptionalBasisFieldMatrix):
    pass
