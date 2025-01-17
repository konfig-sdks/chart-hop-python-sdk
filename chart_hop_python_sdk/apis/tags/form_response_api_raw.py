# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_form_response.get import GetByFormRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_response_form_response_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_response_count.get import GetFormResponseCountRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_response_form_response_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_response_form_response_id.post import UpdateAnswersMetadataRaw
from chart_hop_python_sdk.paths.v1_org_org_id_form_response_form_response_id.patch import UpdateMetadataRaw


class FormResponseApiRaw(
    GetByFormRaw,
    GetByIdRaw,
    GetFormResponseCountRaw,
    RemoveByIdRaw,
    UpdateAnswersMetadataRaw,
    UpdateMetadataRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
