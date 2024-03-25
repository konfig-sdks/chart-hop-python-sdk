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


class RequiredContact(TypedDict):
    # type identifier for the contact
    type: str

    # format for the value
    format: str

class OptionalContact(TypedDict, total=False):
    # value for the contact
    value: str

class Contact(RequiredContact, OptionalContact):
    pass
