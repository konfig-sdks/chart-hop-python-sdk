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


class RequiredInCycleViewFeatures(TypedDict):
    isFinalApprover: bool

    isProposer: bool

    isApprover: bool

    isOwner: bool

    isCollaborator: bool

class OptionalInCycleViewFeatures(TypedDict, total=False):
    isRoot: bool

class InCycleViewFeatures(RequiredInCycleViewFeatures, OptionalInCycleViewFeatures):
    pass
