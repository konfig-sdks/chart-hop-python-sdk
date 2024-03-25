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


class RequiredAppInstallCodeValidateResponse(TypedDict):
    # userId that created the app install authorization code
    userId: str

class OptionalAppInstallCodeValidateResponse(TypedDict, total=False):
    # data associated with the app install authorization code
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # access token issued from app install authorization code
    accessToken: str

class AppInstallCodeValidateResponse(RequiredAppInstallCodeValidateResponse, OptionalAppInstallCodeValidateResponse):
    pass
