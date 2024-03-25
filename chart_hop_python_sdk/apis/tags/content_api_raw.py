# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_content.post import CreateNewPieceRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_content_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_path_path.get import GetByPathRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content.get import GetPaginatedRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_content_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_path_path_render.get import RenderByPathRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_homepage_render.get import RenderHomepageContentsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_homepage.patch import UpdateHomepageContentRaw
from chart_hop_python_sdk.paths.v1_org_org_id_content_content_id.patch import UpdatePieceByIdRaw


class ContentApiRaw(
    CreateNewPieceRaw,
    GetByIdRaw,
    GetByPathRaw,
    GetPaginatedRaw,
    RemoveByIdRaw,
    RenderByPathRaw,
    RenderHomepageContentsRaw,
    UpdateHomepageContentRaw,
    UpdatePieceByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
