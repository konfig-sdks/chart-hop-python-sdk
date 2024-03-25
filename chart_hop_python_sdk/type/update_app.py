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
from chart_hop_python_sdk.type.update_app_allowed_ips import UpdateAppAllowedIps
from chart_hop_python_sdk.type.update_app_events import UpdateAppEvents
from chart_hop_python_sdk.type.update_app_payload import UpdateAppPayload
from chart_hop_python_sdk.type.update_app_redirect_uris import UpdateAppRedirectUris
from chart_hop_python_sdk.type.update_app_scopes import UpdateAppScopes
from chart_hop_python_sdk.type.update_app_tags import UpdateAppTags

class RequiredUpdateApp(TypedDict):
    pass

class OptionalUpdateApp(TypedDict, total=False):
    tags: UpdateAppTags

    # short summary of app
    summary: str

    # human-readable name of app
    title: str

    # full description of app, in Markdown
    description: str

    # short unique name
    name: str

    redirectUris: UpdateAppRedirectUris

    allowedIps: UpdateAppAllowedIps

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

    # current status of app
    status: str

    # minimum access level requested by app
    minAccess: str

    # roleId requested by app
    roleId: str

    # URL that should be notified on events
    eventNotifyUrl: str

    payload: UpdateAppPayload

    events: UpdateAppEvents

    # APP, BUNDLE, or INTERNAL
    type: str

    bundle: Bundle

    scopes: UpdateAppScopes

class UpdateApp(RequiredUpdateApp, OptionalUpdateApp):
    pass
