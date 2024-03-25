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

from chart_hop_python_sdk.type.policy import Policy
from chart_hop_python_sdk.type.role_policy_ids import RolePolicyIds
from chart_hop_python_sdk.type.user import User

class RequiredRole(TypedDict):
    # globally unique id
    id: str

    # human-readable full name of role
    label: str

class OptionalRole(TypedDict, total=False):
    # description of role
    description: str

    # parent organization id (empty if global)
    orgId: str

    policyIds: RolePolicyIds

    # the policies attached to the role
    policies: 'typing.List[Policy]'

    # the users the role is attached to
    users: typing.List[User]

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class Role(RequiredRole, OptionalRole):
    pass
