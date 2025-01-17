# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_assessment_bulk_delete.post import BulkDeleteRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_bulk_duplicate.post import BulkDuplicateAssessmentsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_assessment_id_complete.post import CompleteAssessmentRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment.post import CreateNewAssessmentRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_assessment_id_form_form_id_expire.post import ExpireFormTasksRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment.get import GetAllPaginatedRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_assessment_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_assessment_id_reactivate.post import ReactivateAssessmentRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_assessment_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_bulk_move.post import UpdateAssessmentTypesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_assessment_assessment_id.patch import UpdateExistingAssessmentRaw


class AssessmentApiRaw(
    BulkDeleteRaw,
    BulkDuplicateAssessmentsRaw,
    CompleteAssessmentRaw,
    CreateNewAssessmentRaw,
    ExpireFormTasksRaw,
    GetAllPaginatedRaw,
    GetByIdRaw,
    ReactivateAssessmentRaw,
    RemoveByIdRaw,
    UpdateAssessmentTypesRaw,
    UpdateExistingAssessmentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
