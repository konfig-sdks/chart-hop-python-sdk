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

from chart_hop_python_sdk.type.name import Name
from chart_hop_python_sdk.type.user_list_row_group_ids import UserListRowGroupIds

class RequiredUserListRow(TypedDict):
    name: Name

    inviteStatus: str

    isOrgMember: bool

class OptionalUserListRow(TypedDict, total=False):
    userId: str

    personId: str

    imagePath: str

    email: str

    access: str

    roleLabel: str

    expr: str

    groupIds: UserListRowGroupIds

    loginAt: int

    activeAt: int

class UserListRow(RequiredUserListRow, OptionalUserListRow):
    pass
