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

from chart_hop_python_sdk.type.org_access_group_ids import OrgAccessGroupIds

class RequiredOrgAccess(TypedDict):
    # org id
    orgId: str

    # legacy access permission level
    access: str

class OptionalOrgAccess(TypedDict, total=False):
    # person id, if this user directly corresponds with a person
    personId: str

    groupIds: OrgAccessGroupIds

    # expression that the above access applies to
    expr: str

    # timestamp that this org access will expire
    expireAt: str

    # the role id that defines the users access
    roleId: str

class OrgAccess(RequiredOrgAccess, OptionalOrgAccess):
    pass
