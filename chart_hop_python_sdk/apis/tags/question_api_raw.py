# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_question.post import CreateRaw
from chart_hop_python_sdk.paths.v1_org_org_id_question.get import GetAllInOrgRaw
from chart_hop_python_sdk.paths.v1_org_org_id_question_question_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_question_question_id.delete import RemoveRaw
from chart_hop_python_sdk.paths.v1_org_org_id_question_question_id.patch import UpdateByOrgAndIdRaw


class QuestionApiRaw(
    CreateRaw,
    GetAllInOrgRaw,
    GetByIdRaw,
    RemoveRaw,
    UpdateByOrgAndIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
