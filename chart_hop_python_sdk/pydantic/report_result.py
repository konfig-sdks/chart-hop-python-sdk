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

from chart_hop_python_sdk.pydantic.report_query import ReportQuery
from chart_hop_python_sdk.pydantic.report_query_result import ReportQueryResult

class ReportResult(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent org id
    org_id: str = Field(alias='orgId')

    # identifying key for this report result
    key: str = Field(alias='key')

    # date that the report result interval begins, inclusive
    start_date: date = Field(alias='startDate')

    # date that the report result interval ends, exclusive
    end_date: date = Field(alias='endDate')

    # date that the report result interval ends, exclusive
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='options')

    # list of queries that were requested
    queries: typing.List[ReportQuery] = Field(alias='queries')

    # list of the results, one per query that was requested
    results: typing.List[ReportQueryResult] = Field(alias='results')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # status of the report result
    status: Literal["OK", "LOCKED", "RETRY", "ERROR"] = Field(alias='status')

    # start time of last build
    build_start_at: typing.Optional[str] = Field(None, alias='buildStartAt')

    # end time of last build
    build_end_at: typing.Optional[str] = Field(None, alias='buildEndAt')

    # status or error message
    message: typing.Optional[str] = Field(None, alias='message')

    # percent progress so far
    progress: typing.Optional[typing.Union[int, float]] = Field(None, alias='progress')

    # viewer user id
    view_id: typing.Optional[str] = Field(None, alias='viewId')

    # corresponding report id for the built query
    report_id: typing.Optional[str] = Field(None, alias='reportId')

    # corresponding chart id for the built query
    chart_id: typing.Optional[str] = Field(None, alias='chartId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
