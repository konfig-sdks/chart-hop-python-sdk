# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain.post import CreateChainRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage.post import CreateChainStageRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request.post import CreateRequestRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id.delete import DeleteApprovalChainStageRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id.delete import DeleteChainByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id.delete import DeleteRequestApprovalRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_create_default_chain.post import GenerateDefaultChainStagesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request.get import GetAllApprovalRequestsForApprovalChainRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id.get import GetAllStagesForChainRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id.get import GetApprovalChainByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage.get import GetApprovalChainStagesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain.get import GetApprovalChainsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_entity_comp_review.get import GetCompReviewResponsesForChainRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_entity_scenario.get import GetScenarioResponsesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id_reassign_approver.post import ReassignApproverAtStageRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id.get import RequestApprovalRequestRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id_send_reminder.post import SendStageReviewerReminderRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id.patch import UpdateChainRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id.patch import UpdateExistingRequestRaw
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id.patch import UpdateStageByIdRaw


class ApprovalApiRaw(
    CreateChainRaw,
    CreateChainStageRaw,
    CreateRequestRaw,
    DeleteApprovalChainStageRaw,
    DeleteChainByIdRaw,
    DeleteRequestApprovalRaw,
    GenerateDefaultChainStagesRaw,
    GetAllApprovalRequestsForApprovalChainRaw,
    GetAllStagesForChainRaw,
    GetApprovalChainByIdRaw,
    GetApprovalChainStagesRaw,
    GetApprovalChainsRaw,
    GetCompReviewResponsesForChainRaw,
    GetScenarioResponsesRaw,
    ReassignApproverAtStageRaw,
    RequestApprovalRequestRaw,
    SendStageReviewerReminderRaw,
    UpdateChainRaw,
    UpdateExistingRequestRaw,
    UpdateStageByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
