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

from chart_hop_python_sdk.type.address import Address
from chart_hop_python_sdk.type.group_aliases import GroupAliases
from chart_hop_python_sdk.type.group_lead_job_ids import GroupLeadJobIds
from chart_hop_python_sdk.type.money import Money

class RequiredGroup(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # unique name of group
    name: str

    # unique slug of group
    slug: str

    aliases: GroupAliases

    # type of group
    type: str

    # group fields (currently only description)
    fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalGroup(TypedDict, total=False):
    # external code identifier of the group
    code: str

    leadJobIds: GroupLeadJobIds

    address: Address

    # level of the group, for BAND type only
    level: int

    # Job function category of the group, for DEPARTMENT type only
    func: str

    # Type of the location, for LOCATION type only
    locationType: str

    # parent group id
    parentGroupId: str

    # timezone of the group, for LOCATION type only
    timezone: str

    compMin: Money

    compMax: Money

    # path to profile image
    imagePath: str

    # color of group
    color: str

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

class Group(RequiredGroup, OptionalGroup):
    pass