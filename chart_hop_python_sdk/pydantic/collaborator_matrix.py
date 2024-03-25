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

from chart_hop_python_sdk.pydantic.collaborator_matrix_condition import CollaboratorMatrixCondition
from chart_hop_python_sdk.pydantic.collaborator_matrix_included_fields import CollaboratorMatrixIncludedFields

class CollaboratorMatrix(BaseModel):
    included_fields: CollaboratorMatrixIncludedFields = Field(alias='includedFields')

    conditions: typing.List[CollaboratorMatrixCondition] = Field(alias='conditions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
