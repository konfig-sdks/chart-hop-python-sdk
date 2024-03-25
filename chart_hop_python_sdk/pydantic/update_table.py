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

from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class UpdateTable(BaseModel):
    # name of table
    name: typing.Optional[str] = Field(None, alias='name')

    # human readable label for the table
    label: typing.Optional[str] = Field(None, alias='label')

    # if set, use this column id as the label when referencing rows
    label_column_id: typing.Optional[str] = Field(None, alias='labelColumnId')

    # whether or not the table is time tracked with effective dates (allows time travel or not). If false, then the values set in the table will be the same across all dates.
    effective_dated: typing.Optional[bool] = Field(None, alias='effectiveDated')

    # base sensitivity of this table and entities in it -- should be either ORG or HIGH
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # users who are specifically granted permission to this table
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
