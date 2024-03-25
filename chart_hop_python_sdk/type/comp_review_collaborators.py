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

from chart_hop_python_sdk.type.collaborator_matrix import CollaboratorMatrix
from chart_hop_python_sdk.type.comp_review_collaborators_collaborator_job_ids import CompReviewCollaboratorsCollaboratorJobIds
from chart_hop_python_sdk.type.comp_review_collaborators_job_to_collaborators_map import CompReviewCollaboratorsJobToCollaboratorsMap

class RequiredCompReviewCollaborators(TypedDict):
    # What type of HRBP collaboration the comp review uses
    collaborationType: str

    # What level of access collaborators should have
    collaboratorAccess: str

    jobToCollaboratorsMap: CompReviewCollaboratorsJobToCollaboratorsMap

class OptionalCompReviewCollaborators(TypedDict, total=False):
    collaboratorJobIds: CompReviewCollaboratorsCollaboratorJobIds

    collaboratorMatrix: CollaboratorMatrix

class CompReviewCollaborators(RequiredCompReviewCollaborators, OptionalCompReviewCollaborators):
    pass
