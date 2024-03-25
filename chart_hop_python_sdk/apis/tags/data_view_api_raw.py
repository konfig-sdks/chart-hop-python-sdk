# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_data_view.post import CreateNewDataViewRaw
from chart_hop_python_sdk.paths.v1_org_org_id_data_view_data_view_id.delete import DeleteDataViewRaw
from chart_hop_python_sdk.paths.v1_org_org_id_data_view.get import GetAllPaginatedRaw
from chart_hop_python_sdk.paths.v1_org_org_id_data_view_data_view_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_data_view_data_view_id.patch import UpdateExistingViewRaw


class DataViewApiRaw(
    CreateNewDataViewRaw,
    DeleteDataViewRaw,
    GetAllPaginatedRaw,
    GetByIdRaw,
    UpdateExistingViewRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
