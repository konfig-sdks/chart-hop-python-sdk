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

from chart_hop_python_sdk.pydantic.collaborator_matrix import CollaboratorMatrix
from chart_hop_python_sdk.pydantic.comp_review_collaborators_collaborator_job_ids import CompReviewCollaboratorsCollaboratorJobIds
from chart_hop_python_sdk.pydantic.comp_review_collaborators_job_to_collaborators_map import CompReviewCollaboratorsJobToCollaboratorsMap

class CompReviewCollaborators(BaseModel):
    # What type of HRBP collaboration the comp review uses
    collaboration_type: Literal["NONE", "STATIC", "DYNAMIC"] = Field(alias='collaborationType')

    # What level of access collaborators should have
    collaborator_access: Literal["READ", "EDIT", "SUBMIT"] = Field(alias='collaboratorAccess')

    job_to_collaborators_map: CompReviewCollaboratorsJobToCollaboratorsMap = Field(alias='jobToCollaboratorsMap')

    collaborator_job_ids: typing.Optional[CompReviewCollaboratorsCollaboratorJobIds] = Field(None, alias='collaboratorJobIds')

    collaborator_matrix: typing.Optional[CollaboratorMatrix] = Field(None, alias='collaboratorMatrix')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
