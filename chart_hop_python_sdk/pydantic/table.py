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

class Table(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # name of table
    name: str = Field(alias='name')

    # human readable label for the table
    label: str = Field(alias='label')

    # whether or not the table is time tracked with effective dates (allows time travel or not). If false, then the values set in the table will be the same across all dates.
    effective_dated: bool = Field(alias='effectiveDated')

    # base sensitivity of this table and entities in it -- should be either ORG or HIGH
    sensitive: Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"] = Field(alias='sensitive')

    # users who are specifically granted permission to this table
    share_access: typing.List[ShareAccess] = Field(alias='shareAccess')

    # number of rows in the table
    row_count: int = Field(alias='rowCount')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # last updated by user id
    update_id: str = Field(alias='updateId')

    # last updated timestamp
    update_at: str = Field(alias='updateAt')

    # parent org id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # if set, use this column id as the label when referencing rows
    label_column_id: typing.Optional[str] = Field(None, alias='labelColumnId')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
