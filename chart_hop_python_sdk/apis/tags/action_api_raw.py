# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_action.post import CreateNewActionRaw
from chart_hop_python_sdk.paths.v1_org_org_id_action_action_id.delete import DeleteActionByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_action_action_id_run.post import ExecuteActionForTestingRaw
from chart_hop_python_sdk.paths.v1_org_org_id_action_action_id.get import GetActionByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_action.get import GetAllPaginatedRaw
from chart_hop_python_sdk.paths.v1_org_org_id_action_action_id.patch import UpdateExistingActionByIdRaw


class ActionApiRaw(
    CreateNewActionRaw,
    DeleteActionByIdRaw,
    ExecuteActionForTestingRaw,
    GetActionByIdRaw,
    GetAllPaginatedRaw,
    UpdateExistingActionByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
