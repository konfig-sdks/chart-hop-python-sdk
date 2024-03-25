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

from chart_hop_python_sdk.pydantic.report_metric_collection_item_changes import ReportMetricCollectionItemChanges
from chart_hop_python_sdk.pydantic.report_metric_collection_item_jobs import ReportMetricCollectionItemJobs
from chart_hop_python_sdk.pydantic.report_metric_collection_item_persons import ReportMetricCollectionItemPersons

class ReportMetricCollectionItem(BaseModel):
    changes: ReportMetricCollectionItemChanges = Field(alias='changes')

    jobs: ReportMetricCollectionItemJobs = Field(alias='jobs')

    persons: ReportMetricCollectionItemPersons = Field(alias='persons')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
