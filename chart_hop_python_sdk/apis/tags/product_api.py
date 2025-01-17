# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_product.post import CreateNewProduct
from chart_hop_python_sdk.paths.v1_product_product_id.get import GetById
from chart_hop_python_sdk.paths.v1_product.get import ListAllProducts
from chart_hop_python_sdk.paths.v1_product_product_id.patch import UpdateExistingProduct
from chart_hop_python_sdk.apis.tags.product_api_raw import ProductApiRaw


class ProductApi(
    CreateNewProduct,
    GetById,
    ListAllProducts,
    UpdateExistingProduct,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProductApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProductApiRaw(api_client)
