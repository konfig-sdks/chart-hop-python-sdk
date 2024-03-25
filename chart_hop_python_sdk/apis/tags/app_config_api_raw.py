# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_app_config.post import CreateNewConfigRaw
from chart_hop_python_sdk.paths.v1_app_config_app_id.get import GetDefaultConfigByAppRaw
from chart_hop_python_sdk.paths.v1_app_config_app_id_user_id.get import GetUserConfigByAppAndUserRaw
from chart_hop_python_sdk.paths.v1_app_config_app_id_user_id.patch import UpdateByIdRaw


class AppConfigApiRaw(
    CreateNewConfigRaw,
    GetDefaultConfigByAppRaw,
    GetUserConfigByAppAndUserRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass