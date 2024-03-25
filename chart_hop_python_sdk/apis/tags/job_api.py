# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v2_org_org_id_job.post import CreateNewJob
from chart_hop_python_sdk.paths.v2_org_org_id_job_job_id.get import FindInOrganization
from chart_hop_python_sdk.paths.v2_org_org_id_job.get import FindInOrganization0
from chart_hop_python_sdk.paths.v2_org_org_id_job_count.get import GetOrganizationJobCount
from chart_hop_python_sdk.paths.v2_org_org_id_job_graph.get import GetRegionJobsGraph
from chart_hop_python_sdk.paths.v2_org_org_id_job_graph_counts.get import GetSiblingsAndDirectsMap
from chart_hop_python_sdk.paths.v2_org_org_id_job_job_id_position.get import ListOccupiedPositionsByJobAndDate
from chart_hop_python_sdk.paths.v2_org_org_id_job_bulkupdate.post import PerformBulkUpdate
from chart_hop_python_sdk.paths.v2_org_org_id_job_job_id.delete import RemoveById
from chart_hop_python_sdk.paths.v2_org_org_id_job_job_id.patch import UpdateJobDetails
from chart_hop_python_sdk.apis.tags.job_api_raw import JobApiRaw


class JobApi(
    CreateNewJob,
    FindInOrganization,
    FindInOrganization0,
    GetOrganizationJobCount,
    GetRegionJobsGraph,
    GetSiblingsAndDirectsMap,
    ListOccupiedPositionsByJobAndDate,
    PerformBulkUpdate,
    RemoveById,
    UpdateJobDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: JobApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = JobApiRaw(api_client)