# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_role_role_id_copy.post import CopyExistingRoleRaw
from chart_hop_python_sdk.paths.v1_org_org_id_role.post import CreateNewRoleRaw
from chart_hop_python_sdk.paths.v1_org_org_id_role.get import GetAllInOrgRaw
from chart_hop_python_sdk.paths.v1_org_org_id_role_role_id.get import GetRoleByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_role_role_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_role_role_id.patch import UpdateExistingRaw


class RoleApiRaw(
    CopyExistingRoleRaw,
    CreateNewRoleRaw,
    GetAllInOrgRaw,
    GetRoleByIdRaw,
    RemoveByIdRaw,
    UpdateExistingRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass