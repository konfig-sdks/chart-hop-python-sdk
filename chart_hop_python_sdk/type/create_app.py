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

from chart_hop_python_sdk.type.app_config_field import AppConfigField
from chart_hop_python_sdk.type.bundle import Bundle
from chart_hop_python_sdk.type.create_app_allowed_ips import CreateAppAllowedIps
from chart_hop_python_sdk.type.create_app_events import CreateAppEvents
from chart_hop_python_sdk.type.create_app_payload import CreateAppPayload
from chart_hop_python_sdk.type.create_app_redirect_uris import CreateAppRedirectUris
from chart_hop_python_sdk.type.create_app_scopes import CreateAppScopes
from chart_hop_python_sdk.type.create_app_tags import CreateAppTags

class RequiredCreateApp(TypedDict):
    # short summary of app
    summary: str

    # human-readable name of app
    title: str

    # organization id
    orgId: str

    # short unique name
    name: str

    # execution order of the cron (lower numbers execute earlier)
    cronOrder: int

    # minimum access level requested by app
    minAccess: str

    # APP, BUNDLE, or INTERNAL
    type: str

class OptionalCreateApp(TypedDict, total=False):
    tags: CreateAppTags

    # full description of app, in Markdown
    description: str

    redirectUris: CreateAppRedirectUris

    allowedIps: CreateAppAllowedIps

    # list of configuration fields
    configFields: typing.List[AppConfigField]

    # setup instructions, in Markdown
    setupInstructions: str

    # cron schedule
    cronSchedule: str

    # Day of week if cronSchedule is WEEKLY
    cronDayOfWeek: str

    # path to avatar profile image, should be approximately square dimensions and show logo
    imagePath: str

    # path to larger profile logo image containing brand wordmark, does not need to be square dimensions
    wordmarkImagePath: str

    # path to powered by image, should be approximately square dimensions and show logo
    poweredByImagePath: str

    # current status of app
    status: str

    # roleId requested by app
    roleId: str

    # URL that should be notified on events
    eventNotifyUrl: str

    payload: CreateAppPayload

    events: CreateAppEvents

    bundle: Bundle

    scopes: CreateAppScopes

class CreateApp(RequiredCreateApp, OptionalCreateApp):
    pass
