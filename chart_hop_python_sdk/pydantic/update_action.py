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

from chart_hop_python_sdk.pydantic.action_step import ActionStep
from chart_hop_python_sdk.pydantic.update_action_tags import UpdateActionTags

class UpdateAction(BaseModel):
    tags: typing.Optional[UpdateActionTags] = Field(None, alias='tags')

    # description of the action
    description: typing.Optional[str] = Field(None, alias='description')

    # event pattern to match on, such as change.create.*
    event: typing.Optional[str] = Field(None, alias='event')

    # cron schedule to run on, in crontab format
    cron_schedule: typing.Optional[str] = Field(None, alias='cronSchedule')

    # only run when matching a particular filter
    filter: typing.Optional[str] = Field(None, alias='filter')

    # list of steps to run when matching the event, schedule, and filter
    steps: typing.Optional[typing.List[ActionStep]] = Field(None, alias='steps')

    # status of the action
    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    # whether to run with access to sensitive events or not
    sensitive: typing.Optional[bool] = Field(None, alias='sensitive')

    # organizational category for HRIS-themed actions
    category: typing.Optional[Literal["ONBOARDING", "OFFBOARDING"]] = Field(None, alias='category')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )