# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_stock.get import GetHistory
from chart_hop_python_sdk.paths.v1_stock_symbol_date_type.get import GetPriceByDateType
from chart_hop_python_sdk.paths.v1_stock_id.delete import RemovePrice
from chart_hop_python_sdk.paths.v1_stock_symbol_date_type.put import UpsertPriceByDateType
from chart_hop_python_sdk.apis.tags.stock_api_raw import StockApiRaw


class StockApi(
    GetHistory,
    GetPriceByDateType,
    RemovePrice,
    UpsertPriceByDateType,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: StockApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = StockApiRaw(api_client)
