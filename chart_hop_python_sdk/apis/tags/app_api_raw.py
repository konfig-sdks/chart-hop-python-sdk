# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_app.post import CreateNewAppRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id.get import FindInstalledAppUsersRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install.get import FindInstalledAppUsers0Raw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id_token.post import GenerateOrRegenerateAccessTokenRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id.get import GetActiveAppsByOrgRaw
from chart_hop_python_sdk.paths.v1_app_app_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_app_name_app_name.get import GetByNameRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_name_app_name.get import GetInstalledAppByNameRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id_code.post import GetOauth2AuthorizationCodeRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id_token.get import GetTokenForAppRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id_installdata_install_data_name.get import GetTokenForApp0Raw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install.post import InstallAppForOrgRaw
from chart_hop_python_sdk.paths.v1_app.get import ListPublicGlobalAppsRaw
from chart_hop_python_sdk.paths.v1_app_app_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id_run.post import RunInstalledAppRaw
from chart_hop_python_sdk.paths.v1_app_notify.post import SendEmailNotificationRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id.delete import UninstallAppByUserIdRaw
from chart_hop_python_sdk.paths.v1_app_app_id.patch import UpdateExistingAppRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_app_user_id.patch import UpdateInstalledAppRaw
from chart_hop_python_sdk.paths.v1_app_org_org_id_install_validate.post import ValidateAppInstallationRaw


class AppApiRaw(
    CreateNewAppRaw,
    FindInstalledAppUsersRaw,
    FindInstalledAppUsers0Raw,
    GenerateOrRegenerateAccessTokenRaw,
    GetActiveAppsByOrgRaw,
    GetByIdRaw,
    GetByNameRaw,
    GetInstalledAppByNameRaw,
    GetOauth2AuthorizationCodeRaw,
    GetTokenForAppRaw,
    GetTokenForApp0Raw,
    InstallAppForOrgRaw,
    ListPublicGlobalAppsRaw,
    RemoveByIdRaw,
    RunInstalledAppRaw,
    SendEmailNotificationRaw,
    UninstallAppByUserIdRaw,
    UpdateExistingAppRaw,
    UpdateInstalledAppRaw,
    ValidateAppInstallationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
