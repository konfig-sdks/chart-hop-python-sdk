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


class RequiredFormCollectRequest(TypedDict):
    # Is this a preview?
    preview: bool

class OptionalFormCollectRequest(TypedDict, total=False):
    # the assessment id that this form collection request aligns to (for example a performance review cycle)
    assessmentId: str

    # filter query to apply on who should receive the form collection request
    targetFilter: str

    # Filter to for jobs/person that match via relationship
    submitFilter: str

    # message to include in notification
    message: str

class FormCollectRequest(RequiredFormCollectRequest, OptionalFormCollectRequest):
    pass
