# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_form.post import CreateNewFormRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id.delete import DeleteFormByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_delete.delete import DeleteFormById0Raw
from chart_hop_python_sdk.paths.v1_org_org_id_form_draft_draft_id.delete import DeleteFormDraftRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_person_person_id.get import GetApplicableFormsForPersonRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_draft.get import GetCurrentStateOfDraftDataRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_available.get import ListAvailableFormsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form.get import ListOrgFormsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_render.get import RenderForDisplayRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_rerender_question_update_question_id.post import RerenderQuestionUpdateRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_collect.post import SendEmailsAndChatNotificationsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_remind.post import SendReminderNotificationRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_draft.post import SubmitDraftDataRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_submit.post import SubmitFormDataRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id_submit_draft.post import SubmitFormDraftRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id.post import SubmitFormResponseRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_form_id.patch import UpdateExistingFormRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_status.post import UpdateFormStatusRaw


class FormApiRaw(
    CreateNewFormRaw,
    DeleteFormByIdRaw,
    DeleteFormById0Raw,
    DeleteFormDraftRaw,
    GetApplicableFormsForPersonRaw,
    GetByIdRaw,
    GetCurrentStateOfDraftDataRaw,
    ListAvailableFormsRaw,
    ListOrgFormsRaw,
    RenderForDisplayRaw,
    RerenderQuestionUpdateRaw,
    SendEmailsAndChatNotificationsRaw,
    SendReminderNotificationRaw,
    SubmitDraftDataRaw,
    SubmitFormDataRaw,
    SubmitFormDraftRaw,
    SubmitFormResponseRaw,
    UpdateExistingFormRaw,
    UpdateFormStatusRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
