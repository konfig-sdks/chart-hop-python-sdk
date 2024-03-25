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

class RequiredUpdatePolicy(TypedDict):
    pass

class OptionalUpdatePolicy(TypedDict, total=False):
    # description of policy
    description: str

    # human-readable full name of policy
    label: str

    # the rules that define the policy
    rules: typing.List[PolicyRule]

class UpdatePolicy(RequiredUpdatePolicy, OptionalUpdatePolicy):
    pass
