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

from chart_hop_python_sdk.pydantic.app_config_field import AppConfigField
from chart_hop_python_sdk.pydantic.bundle import Bundle
from chart_hop_python_sdk.pydantic.update_app_allowed_ips import UpdateAppAllowedIps
from chart_hop_python_sdk.pydantic.update_app_events import UpdateAppEvents
from chart_hop_python_sdk.pydantic.update_app_payload import UpdateAppPayload
from chart_hop_python_sdk.pydantic.update_app_redirect_uris import UpdateAppRedirectUris
from chart_hop_python_sdk.pydantic.update_app_scopes import UpdateAppScopes
from chart_hop_python_sdk.pydantic.update_app_tags import UpdateAppTags

class UpdateApp(BaseModel):
    tags: typing.Optional[UpdateAppTags] = Field(None, alias='tags')

    # short summary of app
    summary: typing.Optional[str] = Field(None, alias='summary')

    # human-readable name of app
    title: typing.Optional[str] = Field(None, alias='title')

    # full description of app, in Markdown
    description: typing.Optional[str] = Field(None, alias='description')

    # short unique name
    name: typing.Optional[str] = Field(None, alias='name')

    redirect_uris: typing.Optional[UpdateAppRedirectUris] = Field(None, alias='redirectUris')

    allowed_ips: typing.Optional[UpdateAppAllowedIps] = Field(None, alias='allowedIps')

    # list of configuration fields
    config_fields: typing.Optional[typing.List[AppConfigField]] = Field(None, alias='configFields')

    # setup instructions, in Markdown
    setup_instructions: typing.Optional[str] = Field(None, alias='setupInstructions')

    # execution order of the cron (lower numbers execute earlier)
    cron_order: typing.Optional[int] = Field(None, alias='cronOrder')

    # cron schedule
    cron_schedule: typing.Optional[Literal["DAILY", "WEEKLY"]] = Field(None, alias='cronSchedule')

    # Day of week if cronSchedule is WEEKLY
    cron_day_of_week: typing.Optional[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]] = Field(None, alias='cronDayOfWeek')

    # path to avatar profile image, should be approximately square dimensions and show logo
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    # path to larger profile logo image containing brand wordmark, does not need to be square dimensions
    wordmark_image_path: typing.Optional[str] = Field(None, alias='wordmarkImagePath')

    # path to powered by image, should be approximately square dimensions and show logo
    powered_by_image_path: typing.Optional[str] = Field(None, alias='poweredByImagePath')

    # current status of app
    status: typing.Optional[Literal["GLOBAL", "ACTIVE", "INACTIVE", "DEVELOPMENT"]] = Field(None, alias='status')

    # minimum access level requested by app
    min_access: typing.Optional[Literal["NONE", "VIEW", "LIMITED", "MEMBER_LIMITED_COMP", "MEMBER", "CUSTOM", "TECH_OWNER", "TIMEOFF", "CONTACT", "COMP_CASH", "COMP_EQUITY", "COMP_ALL", "RECRUIT_SENSITIVE", "RECRUIT_PRIMARY", "SENSITIVE_LIMITED_COMP", "SENSITIVE", "PRIMARY", "PEOPLE_OPS_ADMIN", "PEOPLE_OPS_ADMIN_NO_COMP_DATA", "PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA", "OWNER"]] = Field(None, alias='minAccess')

    # roleId requested by app
    role_id: typing.Optional[str] = Field(None, alias='roleId')

    # URL that should be notified on events
    event_notify_url: typing.Optional[str] = Field(None, alias='eventNotifyUrl')

    payload: typing.Optional[UpdateAppPayload] = Field(None, alias='payload')

    events: typing.Optional[UpdateAppEvents] = Field(None, alias='events')

    # APP, BUNDLE, or INTERNAL
    type: typing.Optional[Literal["APP", "BUNDLE", "INTERNAL"]] = Field(None, alias='type')

    bundle: typing.Optional[Bundle] = Field(None, alias='bundle')

    scopes: typing.Optional[UpdateAppScopes] = Field(None, alias='scopes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
