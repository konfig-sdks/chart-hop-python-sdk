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

from chart_hop_python_sdk.type.pair_local_date_local_date import PairLocalDateLocalDate
from chart_hop_python_sdk.type.report_metric_collection_by_query import ReportMetricCollectionByQuery
from chart_hop_python_sdk.type.report_metric_collection_changes import ReportMetricCollectionChanges
from chart_hop_python_sdk.type.report_metric_collection_jobs import ReportMetricCollectionJobs
from chart_hop_python_sdk.type.report_metric_collection_persons import ReportMetricCollectionPersons
from chart_hop_python_sdk.type.report_metric_collection_relevant_fields import ReportMetricCollectionRelevantFields

class RequiredReportMetricCollection(TypedDict):
    relevantFields: ReportMetricCollectionRelevantFields

    changes: ReportMetricCollectionChanges

    jobs: ReportMetricCollectionJobs

    persons: ReportMetricCollectionPersons

    byQuery: ReportMetricCollectionByQuery

class OptionalReportMetricCollection(TypedDict, total=False):
    collectedThrough: PairLocalDateLocalDate

    date: date

class ReportMetricCollection(RequiredReportMetricCollection, OptionalReportMetricCollection):
    pass
