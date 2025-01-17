# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_media_media_id.get import GetMetadataRaw
from chart_hop_python_sdk.paths.v1_org_org_id_media_media_id.get import GetMetadata0Raw
from chart_hop_python_sdk.paths.v1_media.post import UploadNewMediaRaw
from chart_hop_python_sdk.paths.v1_org_org_id_media.post import UploadNewPieceRaw


class MediaApiRaw(
    GetMetadataRaw,
    GetMetadata0Raw,
    UploadNewMediaRaw,
    UploadNewPieceRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
