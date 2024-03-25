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

from chart_hop_python_sdk.type.update_role_policy_ids import UpdateRolePolicyIds

class RequiredUpdateRole(TypedDict):
    pass

class OptionalUpdateRole(TypedDict, total=False):
    # description of role
    description: str

    # human-readable full name of role
    label: str

    policyIds: UpdateRolePolicyIds

class UpdateRole(RequiredUpdateRole, OptionalUpdateRole):
    pass
