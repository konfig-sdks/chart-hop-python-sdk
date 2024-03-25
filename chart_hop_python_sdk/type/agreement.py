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


class RequiredAgreement(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # action taken
    action: str

    # timestamp that the agreement was accepted/cancelled
    createAt: str

    # user id who accepted/cancelled the agreement
    createId: str

class OptionalAgreement(TypedDict, total=False):
    # legal document entity id
    legalDocId: str

class Agreement(RequiredAgreement, OptionalAgreement):
    pass
