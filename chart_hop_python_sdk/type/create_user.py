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

from chart_hop_python_sdk.type.name import Name
from chart_hop_python_sdk.type.org_access import OrgAccess
from chart_hop_python_sdk.type.user_email_setting import UserEmailSetting

class RequiredCreateUser(TypedDict):
    # list of member orgs with permission levels
    orgs: typing.List[OrgAccess]

class OptionalCreateUser(TypedDict, total=False):
    # if the user is an app user, the id of the app
    appId: str

    name: Name

    # email address of user
    email: str

    # path to full-sized profile image in storage
    imagePath: str

    # current status of user
    status: str

    # for apps, options (specific options are specific to the particular app); for users, user-set preferences
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # internal (ChartHop controlled) options
    internalOptions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # write-only secrets; the content of these secrets are not retrievable via the external-facing API
    secrets: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Email settings for the user
    emailSettings: typing.List[UserEmailSetting]

class CreateUser(RequiredCreateUser, OptionalCreateUser):
    pass
