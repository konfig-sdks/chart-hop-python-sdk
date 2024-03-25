# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_change_change_id.patch import AmendScenarioChange
from chart_hop_python_sdk.paths.v1_org_org_id_change_change_id_approve.post import ApproveOrReject
from chart_hop_python_sdk.paths.v1_org_org_id_change_bulkupdate.post import BulkUpdateJobs
from chart_hop_python_sdk.paths.v1_org_org_id_change_change_id_approver.get import CheckApproverEligibility
from chart_hop_python_sdk.paths.v1_org_org_id_change_depart_rehire.post import CreateDepartRehirePair
from chart_hop_python_sdk.paths.v1_org_org_id_change_sync_type.post import CreateIfNotExists
from chart_hop_python_sdk.paths.v1_org_org_id_change_type.post import CreateNewChange
from chart_hop_python_sdk.paths.v1_org_org_id_change_change_id.delete import DeletePreviousChange
from chart_hop_python_sdk.paths.v1_org_org_id_change_scenario_scenario_id.get import FindScenarioChanges
from chart_hop_python_sdk.paths.v1_org_org_id_change_change_id.get import GetById
from chart_hop_python_sdk.paths.v2_org_org_id_change_change_id.get import GetById0
from chart_hop_python_sdk.paths.v1_org_org_id_change.get import GetRecentChanges
from chart_hop_python_sdk.paths.v2_org_org_id_change.get import GetRecentChangesForOrgOrPerson
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_change_change_id_status_process_id.get import GetStatus
from chart_hop_python_sdk.paths.v1_org_org_id_change_bulkchange.post import PerformBulkChange
from chart_hop_python_sdk.paths.v1_org_org_id_change_change_id.patch import UpdateChangeById
from chart_hop_python_sdk.paths.v1_org_org_id_change_type_validate.post import ValidateChangeOperation
from chart_hop_python_sdk.apis.tags.change_api_raw import ChangeApiRaw


class ChangeApi(
    AmendScenarioChange,
    ApproveOrReject,
    BulkUpdateJobs,
    CheckApproverEligibility,
    CreateDepartRehirePair,
    CreateIfNotExists,
    CreateNewChange,
    DeletePreviousChange,
    FindScenarioChanges,
    GetById,
    GetById0,
    GetRecentChanges,
    GetRecentChangesForOrgOrPerson,
    GetStatus,
    PerformBulkChange,
    UpdateChangeById,
    ValidateChangeOperation,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChangeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChangeApiRaw(api_client)