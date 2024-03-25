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
from chart_hop_python_sdk.pydantic.create_app_allowed_ips import CreateAppAllowedIps
from chart_hop_python_sdk.pydantic.create_app_events import CreateAppEvents
from chart_hop_python_sdk.pydantic.create_app_payload import CreateAppPayload
from chart_hop_python_sdk.pydantic.create_app_redirect_uris import CreateAppRedirectUris
from chart_hop_python_sdk.pydantic.create_app_scopes import CreateAppScopes
from chart_hop_python_sdk.pydantic.create_app_tags import CreateAppTags

class CreateApp(BaseModel):
    # short summary of app
    summary: str = Field(alias='summary')

    # human-readable name of app
    title: str = Field(alias='title')

    # organization id
    org_id: str = Field(alias='orgId')

    # short unique name
    name: str = Field(alias='name')

    # execution order of the cron (lower numbers execute earlier)
    cron_order: int = Field(alias='cronOrder')

    # minimum access level requested by app
    min_access: Literal["NONE", "VIEW", "LIMITED", "MEMBER_LIMITED_COMP", "MEMBER", "CUSTOM", "TECH_OWNER", "TIMEOFF", "CONTACT", "COMP_CASH", "COMP_EQUITY", "COMP_ALL", "RECRUIT_SENSITIVE", "RECRUIT_PRIMARY", "SENSITIVE_LIMITED_COMP", "SENSITIVE", "PRIMARY", "PEOPLE_OPS_ADMIN", "PEOPLE_OPS_ADMIN_NO_COMP_DATA", "PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA", "OWNER"] = Field(alias='minAccess')

    # APP, BUNDLE, or INTERNAL
    type: Literal["APP", "BUNDLE", "INTERNAL"] = Field(alias='type')

    tags: typing.Optional[CreateAppTags] = Field(None, alias='tags')

    # full description of app, in Markdown
    description: typing.Optional[str] = Field(None, alias='description')

    redirect_uris: typing.Optional[CreateAppRedirectUris] = Field(None, alias='redirectUris')

    allowed_ips: typing.Optional[CreateAppAllowedIps] = Field(None, alias='allowedIps')

    # list of configuration fields
    config_fields: typing.Optional[typing.List[AppConfigField]] = Field(None, alias='configFields')

    # setup instructions, in Markdown
    setup_instructions: typing.Optional[str] = Field(None, alias='setupInstructions')

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

    # roleId requested by app
    role_id: typing.Optional[str] = Field(None, alias='roleId')

    # URL that should be notified on events
    event_notify_url: typing.Optional[str] = Field(None, alias='eventNotifyUrl')

    payload: typing.Optional[CreateAppPayload] = Field(None, alias='payload')

    events: typing.Optional[CreateAppEvents] = Field(None, alias='events')

    bundle: typing.Optional[Bundle] = Field(None, alias='bundle')

    scopes: typing.Optional[CreateAppScopes] = Field(None, alias='scopes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
