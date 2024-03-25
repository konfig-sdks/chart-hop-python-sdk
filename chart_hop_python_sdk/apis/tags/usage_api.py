# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_usage_type.post import RecordProductFeatureUsage
from chart_hop_python_sdk.apis.tags.usage_api_raw import UsageApiRaw


class UsageApi(
    RecordProductFeatureUsage,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsageApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsageApiRaw(api_client)
