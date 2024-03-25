# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_legaldoc.post import CreateDocument
from chart_hop_python_sdk.paths.v1_legaldoc_name.get import GetByName
from chart_hop_python_sdk.apis.tags.legal_doc_api_raw import LegalDocApiRaw


class LegalDocApi(
    CreateDocument,
    GetByName,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LegalDocApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LegalDocApiRaw(api_client)