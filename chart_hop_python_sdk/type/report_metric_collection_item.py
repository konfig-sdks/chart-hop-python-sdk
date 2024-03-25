# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from chart_hop_python_sdk.type.report_metric_collection_item_changes import ReportMetricCollectionItemChanges
from chart_hop_python_sdk.type.report_metric_collection_item_jobs import ReportMetricCollectionItemJobs
from chart_hop_python_sdk.type.report_metric_collection_item_persons import ReportMetricCollectionItemPersons

class RequiredReportMetricCollectionItem(TypedDict):
    changes: ReportMetricCollectionItemChanges

    jobs: ReportMetricCollectionItemJobs

    persons: ReportMetricCollectionItemPersons

class OptionalReportMetricCollectionItem(TypedDict, total=False):
    pass

class ReportMetricCollectionItem(RequiredReportMetricCollectionItem, OptionalReportMetricCollectionItem):
    pass
