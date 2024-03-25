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

from chart_hop_python_sdk.pydantic.name import Name
from chart_hop_python_sdk.pydantic.org_access import OrgAccess
from chart_hop_python_sdk.pydantic.user_email_setting import UserEmailSetting

class UpdateUser(BaseModel):
    # if the user is an app user, the id of the app
    app_id: typing.Optional[str] = Field(None, alias='appId')

    name: typing.Optional[Name] = Field(None, alias='name')

    # email address of user
    email: typing.Optional[str] = Field(None, alias='email')

    # list of member orgs with permission levels
    orgs: typing.Optional[typing.List[OrgAccess]] = Field(None, alias='orgs')

    # path to full-sized profile image in storage
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    # current status of user
    status: typing.Optional[Literal["SUPERUSER", "NORMAL", "INACTIVE", "UNINSTALLED"]] = Field(None, alias='status')

    # for apps, options (specific options are specific to the particular app); for users, user-set preferences
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    # internal (ChartHop controlled) options
    internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='internalOptions')

    # write-only secrets; the content of these secrets are not retrievable via the external-facing API
    secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='secrets')

    # Email settings for the user
    email_settings: typing.Optional[typing.List[UserEmailSetting]] = Field(None, alias='emailSettings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
