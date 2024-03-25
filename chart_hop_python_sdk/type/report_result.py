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

from chart_hop_python_sdk.type.report_query import ReportQuery
from chart_hop_python_sdk.type.report_query_result import ReportQueryResult

class RequiredReportResult(TypedDict):
    # globally unique id
    id: str

    # parent org id
    orgId: str

    # identifying key for this report result
    key: str

    # date that the report result interval begins, inclusive
    startDate: date

    # date that the report result interval ends, exclusive
    endDate: date

    # date that the report result interval ends, exclusive
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # list of queries that were requested
    queries: typing.List[ReportQuery]

    # list of the results, one per query that was requested
    results: typing.List[ReportQueryResult]

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # status of the report result
    status: str

class OptionalReportResult(TypedDict, total=False):
    # start time of last build
    buildStartAt: str

    # end time of last build
    buildEndAt: str

    # status or error message
    message: str

    # percent progress so far
    progress: typing.Union[int, float]

    # viewer user id
    viewId: str

    # corresponding report id for the built query
    reportId: str

    # corresponding chart id for the built query
    chartId: str

class ReportResult(RequiredReportResult, OptionalReportResult):
    pass
