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

from chart_hop_python_sdk.type.form import Form
from chart_hop_python_sdk.type.question import Question

class RequiredFormVersion(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # form id
    formId: str

class OptionalFormVersion(TypedDict, total=False):
    form: Form

    # questions contained in form, at the time of version creation
    questions: typing.List[Question]

    # created timestamp
    createAt: str

class FormVersion(RequiredFormVersion, OptionalFormVersion):
    pass
