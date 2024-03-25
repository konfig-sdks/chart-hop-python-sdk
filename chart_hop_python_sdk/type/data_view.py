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

from chart_hop_python_sdk.type.data_view_column_widths import DataViewColumnWidths
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredDataView(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # data view name
    name: str

    # slug for URL
    slug: str

class OptionalDataView(TypedDict, total=False):
    # comma delimited list of columns
    columns: str

    # type of data view
    type: str

    # entity type being viewed
    entityType: str

    columnWidths: DataViewColumnWidths

    # date of view, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    date: str

    # start date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    startDate: str

    # end date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    endDate: str

    # filter query
    filter: str

    # comma delimited list of columns by which to sort
    sort: str

    # column to group duplicates by
    groupBy: str

    # users who are specifically granted permission to view or edit this data view
    shareAccess: typing.List[ShareAccess]

    # sensitivity level of data view
    sensitive: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class DataView(RequiredDataView, OptionalDataView):
    pass
