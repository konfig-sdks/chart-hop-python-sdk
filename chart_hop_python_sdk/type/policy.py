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

from chart_hop_python_sdk.type.policy_rule import PolicyRule
from chart_hop_python_sdk.type.role import Role
from chart_hop_python_sdk.type.user import User

class RequiredPolicy(TypedDict):
    # globally unique id
    id: str

    # human-readable full name of policy
    label: str

class OptionalPolicy(TypedDict, total=False):
    # description of policy
    description: str

    # parent organization id (empty if global)
    orgId: str

    # the rules that define the policy
    rules: typing.List[PolicyRule]

    # the roles the policy is attached to
    roles: 'typing.List[Role]'

    # the users the policy is attached to
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

class Policy(RequiredPolicy, OptionalPolicy):
    pass
