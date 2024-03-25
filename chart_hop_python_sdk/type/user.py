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

from chart_hop_python_sdk.type.bundle_install import BundleInstall
from chart_hop_python_sdk.type.name import Name
from chart_hop_python_sdk.type.org_access import OrgAccess
from chart_hop_python_sdk.type.user_email_setting import UserEmailSetting
from chart_hop_python_sdk.type.web_registered_credential import WebRegisteredCredential

class RequiredUser(TypedDict):
    # globally unique id
    id: str

    name: Name

class OptionalUser(TypedDict, total=False):
    # job title, if available
    title: str

    # if the user is an app user, the id of the app
    appId: str

    # email address of user
    email: str

    # password of user (encrypted)
    password: str

    # list of member orgs with permission levels
    orgs: typing.List[OrgAccess]

    # path to full-sized profile image in storage
    imagePath: str

    # current status of user
    status: str

    # type of user
    type: str

    # for apps, options (specific options are specific to the particular app); for users, user-set preferences
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # internal (ChartHop controlled) options
    internalOptions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    bundleInstall: BundleInstall

    # write-only secrets; the content of these secrets are not retrievable via the external-facing API
    secrets: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # last activity timestamp
    activeAt: str

    # last login timestamp
    loginAt: str

    # number of consecutive failed logins
    loginFailCount: int

    # last IP address used
    remoteIp: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # email verified timestamp, if the email has been verified
    verifyAt: str

    # list of registered 2FA registered credentials
    mfas: typing.List[WebRegisteredCredential]

    # Email settings for the user
    emailSettings: typing.List[UserEmailSetting]

class User(RequiredUser, OptionalUser):
    pass
