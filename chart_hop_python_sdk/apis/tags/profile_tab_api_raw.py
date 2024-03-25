# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab.post import CreateNewTabRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab_profile_tab_id.delete import DeleteProfileTabRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab_job_job_id.get import FindTabsForJobRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab_profile_tab_id.get import GetByOrgIdAndTabIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab_job_job_id_profile_tab_tab_id.get import GetEvaluateProfileTabContentRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab_person_person_id.get import GetProfileTabsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab.get import ListProfileTabsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_profile_tab_profile_tab_id.patch import UpdateExistingTabRaw


class ProfileTabApiRaw(
    CreateNewTabRaw,
    DeleteProfileTabRaw,
    FindTabsForJobRaw,
    GetByOrgIdAndTabIdRaw,
    GetEvaluateProfileTabContentRaw,
    GetProfileTabsRaw,
    ListProfileTabsRaw,
    UpdateExistingTabRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
