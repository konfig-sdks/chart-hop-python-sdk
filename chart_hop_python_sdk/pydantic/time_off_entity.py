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


class TimeOffEntity(BaseModel):
    # globally unique id of time off
    id: str = Field(alias='id')

    # org that the time off belongs to
    org_id: str = Field(alias='orgId')

    # person taking the time off
    person_id: str = Field(alias='personId')

    # start date of time off, inclusive
    start_date: date = Field(alias='startDate')

    # end date of time off, inclusive
    end_date: date = Field(alias='endDate')

    # external identifier, if time off synced from external system
    external_id: typing.Optional[str] = Field(None, alias='externalId')

    # number of days used
    days: typing.Optional[typing.Union[int, float]] = Field(None, alias='days')

    # number of hours used
    hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='hours')

    # type of time off
    type_description: typing.Optional[str] = Field(None, alias='typeDescription')

    # notes on the time off
    note: typing.Optional[str] = Field(None, alias='note')

    # approval status of the time off
    approval: typing.Optional[Literal["APPROVED", "PENDING", "CANCELLED", "REJECTED", "SUPERSEDED"]] = Field(None, alias='approval')

    # timestamp of approval
    approval_at: typing.Optional[str] = Field(None, alias='approvalAt')

    # user who either is the next one requesting approval, or the user who did the final approval or rejection
    approval_user_id: typing.Optional[str] = Field(None, alias='approvalUserId')

    # requested at timestamp -- often the same as createAt
    request_at: typing.Optional[str] = Field(None, alias='requestAt')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
