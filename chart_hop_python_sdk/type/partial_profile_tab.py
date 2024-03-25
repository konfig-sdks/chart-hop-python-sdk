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

from chart_hop_python_sdk.type.block import Block

class RequiredPartialProfileTab(TypedDict):
    pass

class OptionalPartialProfileTab(TypedDict, total=False):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable name of profile tab
    label: str

    # ordered list of blocks contained by profile tab
    blocks: typing.List[Block]

    # status of the profile tab
    status: str

    # filter that controls on which profiles this tab will appear
    targetFilter: str

    # filter that controls which viewers can read this profile tab. The profileTab:read permission, if present, overrides this filter
    readFilter: str

    # sort order
    sort: int

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

class PartialProfileTab(RequiredPartialProfileTab, OptionalPartialProfileTab):
    pass
