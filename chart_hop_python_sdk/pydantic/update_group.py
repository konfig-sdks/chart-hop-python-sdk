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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.address import Address
from chart_hop_python_sdk.pydantic.money import Money
from chart_hop_python_sdk.pydantic.update_group_aliases import UpdateGroupAliases
from chart_hop_python_sdk.pydantic.update_group_lead_job_ids import UpdateGroupLeadJobIds

class UpdateGroup(BaseModel):
    # unique name of group
    name: typing.Optional[str] = Field(None, alias='name')

    # unique slug of group
    slug: typing.Optional[str] = Field(None, alias='slug')

    # external code identifier of the group
    code: typing.Optional[str] = Field(None, alias='code')

    aliases: typing.Optional[UpdateGroupAliases] = Field(None, alias='aliases')

    lead_job_ids: typing.Optional[UpdateGroupLeadJobIds] = Field(None, alias='leadJobIds')

    # group fields (currently only description)
    fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='fields')

    address: typing.Optional[Address] = Field(None, alias='address')

    # level of the group, for BAND type only
    level: typing.Optional[int] = Field(None, alias='level')

    # Job function category of the group, for DEPARTMENT type only
    func: typing.Optional[Literal["BD", "CS", "DESIGN", "ENGINEERING", "EXECUTIVE", "FINANCE", "GENERAL", "IT", "LEGAL", "MARKETING", "OPERATIONS", "PEOPLE", "PRODUCT", "RECRUITING", "SALES", "SECURITY", "SUPPORT"]] = Field(None, alias='func')

    # Type of the location, for LOCATION type only
    location_type: typing.Optional[Literal["OFFICE", "REMOTE"]] = Field(None, alias='locationType')

    # parent group id
    parent_group_id: typing.Optional[str] = Field(None, alias='parentGroupId')

    # timezone of the group, for LOCATION type only
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    comp_min: typing.Optional[Money] = Field(None, alias='compMin')

    comp_max: typing.Optional[Money] = Field(None, alias='compMax')

    # path to profile image
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    # color of group
    color: typing.Optional[str] = Field(None, alias='color')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
