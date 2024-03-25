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

class Assessment(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # human-readable label of assessment
    label: str = Field(alias='label')

    # unique slug of assessment
    slug: str = Field(alias='slug')

    # type of assessment
    type: Literal["REVIEW", "COMP_REVIEW", "SURVEY"] = Field(alias='type')

    # assessment fields (description)
    fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='fields')

    # users who have been granted access to this assessment
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # view sensitivity of this assessment
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # color of assessment
    color: typing.Optional[str] = Field(None, alias='color')

    # Date this assessment begins. In the context of REVIEW goals, the date the review cycle begins.
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    # Date this assessment ends, or is completed. In the context of REVIEW assessment, the date the review cycle ends.
    end_date: typing.Optional[date] = Field(None, alias='endDate')

    # status of this assessment - DRAFT, ACTIVE, DONE
    status: typing.Optional[Literal["DRAFT", "ACTIVE", "DONE"]] = Field(None, alias='status')

    # timestamp when the status of this assessment was set to done
    done_at: typing.Optional[str] = Field(None, alias='doneAt')

    # number of tasks associated with this assessment
    task_count: typing.Optional[int] = Field(None, alias='taskCount')

    # number of tasks associated with this assessment that are done
    task_done_count: typing.Optional[int] = Field(None, alias='taskDoneCount')

    # number of people included in this assessment
    people_included_count: typing.Optional[int] = Field(None, alias='peopleIncludedCount')

    # Query for which people/jobs can be included in the review.
    query: typing.Optional[str] = Field(None, alias='query')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
