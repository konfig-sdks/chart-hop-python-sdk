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


class RequiredFormDraft(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # form being submitted
    formId: str

    # draft submission data - map of field names to data
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalFormDraft(TypedDict, total=False):
    # person form is being filled out on
    personId: str

    pendingApprovalChangeId: str

class FormDraft(RequiredFormDraft, OptionalFormDraft):
    pass
