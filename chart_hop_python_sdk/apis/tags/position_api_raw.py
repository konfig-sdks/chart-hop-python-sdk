# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id_job_job_id.post import AssignJobToPositionRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position.post import CreateNewPositionRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id_purge.delete import DeleteAndPurgeRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id.delete import DeletePositionRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id_history.get import GetHistoryByIdRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_import.post import ImportCsvDataWithFilePathRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position.get import ListRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id_job_job_id.delete import RemoveJobFromPositionRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id_job_job_id.patch import UpdateJobDatesOnPositionRaw
from chart_hop_python_sdk.paths.v2_org_org_id_position_position_id.patch import UpdatePositionDetailsRaw


class PositionApiRaw(
    AssignJobToPositionRaw,
    CreateNewPositionRaw,
    DeleteAndPurgeRaw,
    DeletePositionRaw,
    GetByIdRaw,
    GetHistoryByIdRaw,
    ImportCsvDataWithFilePathRaw,
    ListRaw,
    RemoveJobFromPositionRaw,
    UpdateJobDatesOnPositionRaw,
    UpdatePositionDetailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
