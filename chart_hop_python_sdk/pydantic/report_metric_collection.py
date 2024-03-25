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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.pair_local_date_local_date import PairLocalDateLocalDate
from chart_hop_python_sdk.pydantic.report_metric_collection_by_query import ReportMetricCollectionByQuery
from chart_hop_python_sdk.pydantic.report_metric_collection_changes import ReportMetricCollectionChanges
from chart_hop_python_sdk.pydantic.report_metric_collection_jobs import ReportMetricCollectionJobs
from chart_hop_python_sdk.pydantic.report_metric_collection_persons import ReportMetricCollectionPersons
from chart_hop_python_sdk.pydantic.report_metric_collection_relevant_fields import ReportMetricCollectionRelevantFields

class ReportMetricCollection(BaseModel):
    relevant_fields: ReportMetricCollectionRelevantFields = Field(alias='relevantFields')

    changes: ReportMetricCollectionChanges = Field(alias='changes')

    jobs: ReportMetricCollectionJobs = Field(alias='jobs')

    persons: ReportMetricCollectionPersons = Field(alias='persons')

    by_query: ReportMetricCollectionByQuery = Field(alias='byQuery')

    collected_through: typing.Optional[PairLocalDateLocalDate] = Field(None, alias='collectedThrough')

    date: typing.Optional[date] = Field(None, alias='date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
