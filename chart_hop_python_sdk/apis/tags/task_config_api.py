# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_task_config.post import CreateNewConfig
from chart_hop_python_sdk.paths.v1_org_org_id_task_config.get import GetAllConfigs
from chart_hop_python_sdk.paths.v1_org_org_id_task_config_id.get import GetSpecificConfig
from chart_hop_python_sdk.apis.tags.task_config_api_raw import TaskConfigApiRaw


class TaskConfigApi(
    CreateNewConfig,
    GetAllConfigs,
    GetSpecificConfig,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TaskConfigApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TaskConfigApiRaw(api_client)
