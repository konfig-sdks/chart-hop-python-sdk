# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_category.post import CreateNewCategory
from chart_hop_python_sdk.paths.v1_org_org_id_category.get import GetAvailable
from chart_hop_python_sdk.paths.v1_org_org_id_category_category_id.get import GetById
from chart_hop_python_sdk.paths.v1_org_org_id_category_category_id.delete import RemoveById
from chart_hop_python_sdk.paths.v1_org_org_id_category_category_id.patch import UpdateExistingCategory
from chart_hop_python_sdk.apis.tags.category_api_raw import CategoryApiRaw


class CategoryApi(
    CreateNewCategory,
    GetAvailable,
    GetById,
    RemoveById,
    UpdateExistingCategory,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CategoryApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CategoryApiRaw(api_client)
