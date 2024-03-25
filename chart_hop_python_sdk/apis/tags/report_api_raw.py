# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_report_bulk_delete.post import BulkDeleteRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_report_id_clone.post import CreateExactCopyRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report.post import CreateNewReportRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_bulk_duplicate.post import DuplicateReportsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_report_id_chart_chart_id_export_csv.post import ExportChartCsvRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_report_id.get import FindReportByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report.get import GetAllPaginatedRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_report_id_query.get import GetAllReportChartsRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_count.get import GetCountOfReportsInOrganizationRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_report_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_query.post import TimeseriesDataArbitraryQueriesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_report_report_id.patch import UpdateExistingReportRaw


class ReportApiRaw(
    BulkDeleteRaw,
    CreateExactCopyRaw,
    CreateNewReportRaw,
    DuplicateReportsRaw,
    ExportChartCsvRaw,
    FindReportByIdRaw,
    GetAllPaginatedRaw,
    GetAllReportChartsRaw,
    GetCountOfReportsInOrganizationRaw,
    RemoveByIdRaw,
    TimeseriesDataArbitraryQueriesRaw,
    UpdateExistingReportRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
