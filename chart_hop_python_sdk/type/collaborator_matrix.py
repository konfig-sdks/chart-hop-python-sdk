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

from chart_hop_python_sdk.type.collaborator_matrix_condition import CollaboratorMatrixCondition
from chart_hop_python_sdk.type.collaborator_matrix_included_fields import CollaboratorMatrixIncludedFields

class RequiredCollaboratorMatrix(TypedDict):
    includedFields: CollaboratorMatrixIncludedFields

    conditions: typing.List[CollaboratorMatrixCondition]

class OptionalCollaboratorMatrix(TypedDict, total=False):
    pass

class CollaboratorMatrix(RequiredCollaboratorMatrix, OptionalCollaboratorMatrix):
    pass
