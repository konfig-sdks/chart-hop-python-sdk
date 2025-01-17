# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_email_template.post import CreateNewTemplate
from chart_hop_python_sdk.paths.v1_email_template_non_essential.get import GetAllNonEssential
from chart_hop_python_sdk.paths.v1_email_template_name_name.get import GetByName
from chart_hop_python_sdk.paths.v1_email_template_essential.get import ListEssentialEmailTemplates
from chart_hop_python_sdk.paths.v1_email_template_email_template_id.patch import UpdateExistingTemplate
from chart_hop_python_sdk.apis.tags.email_template_api_raw import EmailTemplateApiRaw


class EmailTemplateApi(
    CreateNewTemplate,
    GetAllNonEssential,
    GetByName,
    ListEssentialEmailTemplates,
    UpdateExistingTemplate,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmailTemplateApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmailTemplateApiRaw(api_client)
