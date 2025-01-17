# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_task_bulk_delete.delete import DeleteBulkTasks
from chart_hop_python_sdk.paths.v1_org_org_id_task.get import GetAllTasks
from chart_hop_python_sdk.paths.v1_org_org_id_task_summary_assessment_id.get import GetAssessmentTasksSummary
from chart_hop_python_sdk.paths.v1_org_org_id_task_me.get import GetCurrentUserTasks
from chart_hop_python_sdk.paths.v1_org_org_id_task_task_id_skip.patch import MarkAsSkipped
from chart_hop_python_sdk.paths.v1_org_org_id_task_task.get import QueryAssessmentTasks
from chart_hop_python_sdk.paths.v1_org_org_id_task_task_id.delete import RemoveById
from chart_hop_python_sdk.paths.v1_org_org_id_task_assessment_id_form_id.delete import RemoveFormFromAssessment
from chart_hop_python_sdk.paths.v1_org_org_id_task_remind.post import SendReminderNotification
from chart_hop_python_sdk.paths.v1_org_org_id_task_task_id_mark_done.patch import UpdateStatus
from chart_hop_python_sdk.apis.tags.task_api_raw import TaskApiRaw


class TaskApi(
    DeleteBulkTasks,
    GetAllTasks,
    GetAssessmentTasksSummary,
    GetCurrentUserTasks,
    MarkAsSkipped,
    QueryAssessmentTasks,
    RemoveById,
    RemoveFormFromAssessment,
    SendReminderNotification,
    UpdateStatus,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TaskApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TaskApiRaw(api_client)
