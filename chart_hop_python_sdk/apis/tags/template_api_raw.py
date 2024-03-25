# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_template_bulk_delete.post import BulkDeleteRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_bulk_duplicate.post import CreateBulkDuplicateRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_email.post import CreateEmailRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template.post import CreateNewTemplateRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_template_id_render.post import EvaluateAgainstJobRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_template_id_generate.post import GeneratePdfsAndEmailsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_template_id_preview.post import GenerateTemplatePreviewRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template.get import GetAllInOrgsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_template_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_email_template_name.get import GetByNameRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_template_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_email_template_name.delete import RemoveEmailRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_email_template_name.patch import UpdateEmailTemplateRaw
from chart_hop_python_sdk.paths.v1_org_org_id_template_template_id.patch import UpdateExistingRaw


class TemplateApiRaw(
    BulkDeleteRaw,
    CreateBulkDuplicateRaw,
    CreateEmailRaw,
    CreateNewTemplateRaw,
    EvaluateAgainstJobRaw,
    GeneratePdfsAndEmailsRaw,
    GenerateTemplatePreviewRaw,
    GetAllInOrgsRaw,
    GetByIdRaw,
    GetByNameRaw,
    RemoveByIdRaw,
    RemoveEmailRaw,
    UpdateEmailTemplateRaw,
    UpdateExistingRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass