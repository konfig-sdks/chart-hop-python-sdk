# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_email_template.post import CreateNewTemplateRaw
from chart_hop_python_sdk.paths.v1_email_template_non_essential.get import GetAllNonEssentialRaw
from chart_hop_python_sdk.paths.v1_email_template_name_name.get import GetByNameRaw
from chart_hop_python_sdk.paths.v1_email_template_essential.get import ListEssentialEmailTemplatesRaw
from chart_hop_python_sdk.paths.v1_email_template_email_template_id.patch import UpdateExistingTemplateRaw


class EmailTemplateApiRaw(
    CreateNewTemplateRaw,
    GetAllNonEssentialRaw,
    GetByNameRaw,
    ListEssentialEmailTemplatesRaw,
    UpdateExistingTemplateRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
