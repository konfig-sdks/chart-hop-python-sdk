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

from chart_hop_python_sdk.pydantic.create_data_view_column_widths import CreateDataViewColumnWidths
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class CreateDataView(BaseModel):
    # data view name
    name: str = Field(alias='name')

    # comma delimited list of columns
    columns: typing.Optional[str] = Field(None, alias='columns')

    # type of data view
    type: typing.Optional[Literal["ANY", "DATA_SHEET", "ORG_CHART", "MAP"]] = Field(None, alias='type')

    # entity type being viewed
    entity_type: typing.Optional[str] = Field(None, alias='entityType')

    column_widths: typing.Optional[CreateDataViewColumnWidths] = Field(None, alias='columnWidths')

    # date of view, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    date: typing.Optional[str] = Field(None, alias='date')

    # start date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # end date of view, if displaying a date range, in either relative (-7d) or exact (YYYY-MM-DD) format; if not present, defaults to today
    end_date: typing.Optional[str] = Field(None, alias='endDate')

    # filter query
    filter: typing.Optional[str] = Field(None, alias='filter')

    # comma delimited list of columns by which to sort
    sort: typing.Optional[str] = Field(None, alias='sort')

    # column to group duplicates by
    group_by: typing.Optional[str] = Field(None, alias='groupBy')

    # users who are specifically granted permission to view or edit this data view
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # sensitivity level of data view
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
