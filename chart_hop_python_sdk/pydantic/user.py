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

from chart_hop_python_sdk.pydantic.bundle_install import BundleInstall
from chart_hop_python_sdk.pydantic.name import Name
from chart_hop_python_sdk.pydantic.org_access import OrgAccess
from chart_hop_python_sdk.pydantic.user_email_setting import UserEmailSetting
from chart_hop_python_sdk.pydantic.web_registered_credential import WebRegisteredCredential

class User(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    name: Name = Field(alias='name')

    # job title, if available
    title: typing.Optional[str] = Field(None, alias='title')

    # if the user is an app user, the id of the app
    app_id: typing.Optional[str] = Field(None, alias='appId')

    # email address of user
    email: typing.Optional[str] = Field(None, alias='email')

    # password of user (encrypted)
    password: typing.Optional[str] = Field(None, alias='password')

    # list of member orgs with permission levels
    orgs: typing.Optional[typing.List[OrgAccess]] = Field(None, alias='orgs')

    # path to full-sized profile image in storage
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    # current status of user
    status: typing.Optional[Literal["SUPERUSER", "NORMAL", "INACTIVE", "UNINSTALLED"]] = Field(None, alias='status')

    # type of user
    type: typing.Optional[Literal["USER", "APP"]] = Field(None, alias='type')

    # for apps, options (specific options are specific to the particular app); for users, user-set preferences
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    # internal (ChartHop controlled) options
    internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='internalOptions')

    bundle_install: typing.Optional[BundleInstall] = Field(None, alias='bundleInstall')

    # write-only secrets; the content of these secrets are not retrievable via the external-facing API
    secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='secrets')

    # last activity timestamp
    active_at: typing.Optional[str] = Field(None, alias='activeAt')

    # last login timestamp
    login_at: typing.Optional[str] = Field(None, alias='loginAt')

    # number of consecutive failed logins
    login_fail_count: typing.Optional[int] = Field(None, alias='loginFailCount')

    # last IP address used
    remote_ip: typing.Optional[str] = Field(None, alias='remoteIp')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # email verified timestamp, if the email has been verified
    verify_at: typing.Optional[str] = Field(None, alias='verifyAt')

    # list of registered 2FA registered credentials
    mfas: typing.Optional[typing.List[WebRegisteredCredential]] = Field(None, alias='mfas')

    # Email settings for the user
    email_settings: typing.Optional[typing.List[UserEmailSetting]] = Field(None, alias='emailSettings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
