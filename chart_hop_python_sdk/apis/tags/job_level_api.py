# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_job_level.post import CreateNewJobLevel
from chart_hop_python_sdk.paths.v1_org_org_id_job_level_job_level_id.delete import DeleteJobLevel
from chart_hop_python_sdk.paths.v1_org_org_id_job_level.get import FindInOrganization
from chart_hop_python_sdk.paths.v1_org_org_id_job_level_job_level_id.get import GetByEffectiveDate
from chart_hop_python_sdk.paths.v1_org_org_id_job_level_job_level_id.patch import UpdateJobLevel
from chart_hop_python_sdk.apis.tags.job_level_api_raw import JobLevelApiRaw


class JobLevelApi(
    CreateNewJobLevel,
    DeleteJobLevel,
    FindInOrganization,
    GetByEffectiveDate,
    UpdateJobLevel,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: JobLevelApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = JobLevelApiRaw(api_client)
