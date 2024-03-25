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
from chart_hop_python_sdk.pydantic.contact import Contact
from chart_hop_python_sdk.pydantic.name import Name
from chart_hop_python_sdk.pydantic.org_access import OrgAccess
from chart_hop_python_sdk.pydantic.person_fields import PersonFields

class Person(BaseModel):
    # unique id
    id: str = Field(alias='id')

    name: Name = Field(alias='name')

    # parent org id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # user id, if this person corresponds with a user
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # contacts (emails, phones, external ids)
    contacts: typing.Optional[typing.List[Contact]] = Field(None, alias='contacts')

    address: typing.Optional[Address] = Field(None, alias='address')

    remote_work_address: typing.Optional[Address] = Field(None, alias='remoteWorkAddress')

    # birthdate
    birth_date: typing.Optional[str] = Field(None, alias='birthDate')

    # start date of most recent hire
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # end date of most recent hire
    end_date: typing.Optional[str] = Field(None, alias='endDate')

    # path to full-sized profile image in storage
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    # path to pronunciation of the person's name
    name_audio_path: typing.Optional[str] = Field(None, alias='nameAudioPath')

    # self-reported gender
    gender: typing.Optional[Literal["MALE", "FEMALE", "NONBINARY", "PREFER_NOT"]] = Field(None, alias='gender')

    # self-reported ethnicity
    ethnicity: typing.Optional[Literal["HISPANIC", "WHITE", "BLACK", "PACIFIC", "ASIAN", "NATIVE", "TWO", "PREFER_NOT"]] = Field(None, alias='ethnicity')

    fields: typing.Optional[PersonFields] = Field(None, alias='fields')

    # personal sensitivity preferences around specific fields
    sensitive_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='sensitiveFields')

    # sort order
    sort: typing.Optional[str] = Field(None, alias='sort')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    invite_options: typing.Optional[OrgAccess] = Field(None, alias='inviteOptions')

    # current status within the organization
    state: typing.Optional[Literal["PRIMARY", "SCENARIO", "PENDING", "INACTIVE"]] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
