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

from chart_hop_python_sdk.type.app_allowed_ips import AppAllowedIps
from chart_hop_python_sdk.type.app_config_field import AppConfigField
from chart_hop_python_sdk.type.app_events import AppEvents
from chart_hop_python_sdk.type.app_payload import AppPayload
from chart_hop_python_sdk.type.app_redirect_uris import AppRedirectUris
from chart_hop_python_sdk.type.app_scopes import AppScopes
from chart_hop_python_sdk.type.app_tags import AppTags
from chart_hop_python_sdk.type.bundle import Bundle

class RequiredApp(TypedDict):
    # short summary of app
    summary: str

    # human-readable name of app
    title: str

    # globally unique id
    id: str

    # organization id
    orgId: str

    # short unique name
    name: str

    # current status of app
    status: str

    # minimum access level requested by app
    minAccess: str

class OptionalApp(TypedDict, total=False):
    tags: AppTags

    # full description of app, in Markdown
    description: str

    redirectUris: AppRedirectUris

    allowedIps: AppAllowedIps

    # list of configuration fields
    configFields: typing.List[AppConfigField]

    # setup instructions, in Markdown
    setupInstructions: str

    # execution order of the cron (lower numbers execute earlier)
    cronOrder: int

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

    # roleId requested by app
    roleId: str

    # URL that should be notified on events
    eventNotifyUrl: str

    payload: AppPayload

    events: AppEvents

    # APP, BUNDLE, or INTERNAL
    type: str

    bundle: Bundle

    scopes: AppScopes

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

class App(RequiredApp, OptionalApp):
    pass
