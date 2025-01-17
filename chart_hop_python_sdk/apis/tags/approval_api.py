# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain.post import CreateChain
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage.post import CreateChainStage
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request.post import CreateRequest
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id.delete import DeleteApprovalChainStage
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id.delete import DeleteChainById
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id.delete import DeleteRequestApproval
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_create_default_chain.post import GenerateDefaultChainStages
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request.get import GetAllApprovalRequestsForApprovalChain
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id.get import GetAllStagesForChain
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id.get import GetApprovalChainById
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage.get import GetApprovalChainStages
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain.get import GetApprovalChains
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_entity_comp_review.get import GetCompReviewResponsesForChain
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_entity_scenario.get import GetScenarioResponses
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id_reassign_approver.post import ReassignApproverAtStage
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id.get import RequestApprovalRequest
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id_send_reminder.post import SendStageReviewerReminder
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id.patch import UpdateChain
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_request_approval_request_id.patch import UpdateExistingRequest
from chart_hop_python_sdk.paths.v1_org_org_id_approval_chain_approval_chain_id_stage_approval_chain_stage_id.patch import UpdateStageById
from chart_hop_python_sdk.apis.tags.approval_api_raw import ApprovalApiRaw


class ApprovalApi(
    CreateChain,
    CreateChainStage,
    CreateRequest,
    DeleteApprovalChainStage,
    DeleteChainById,
    DeleteRequestApproval,
    GenerateDefaultChainStages,
    GetAllApprovalRequestsForApprovalChain,
    GetAllStagesForChain,
    GetApprovalChainById,
    GetApprovalChainStages,
    GetApprovalChains,
    GetCompReviewResponsesForChain,
    GetScenarioResponses,
    ReassignApproverAtStage,
    RequestApprovalRequest,
    SendStageReviewerReminder,
    UpdateChain,
    UpdateExistingRequest,
    UpdateStageById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ApprovalApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ApprovalApiRaw(api_client)
