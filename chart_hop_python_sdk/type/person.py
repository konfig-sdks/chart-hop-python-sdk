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
from chart_hop_python_sdk.type.contact import Contact
from chart_hop_python_sdk.type.name import Name
from chart_hop_python_sdk.type.org_access import OrgAccess
from chart_hop_python_sdk.type.person_fields import PersonFields

class RequiredPerson(TypedDict):
    # unique id
    id: str

    name: Name

class OptionalPerson(TypedDict, total=False):
    # parent org id
    orgId: str

    # user id, if this person corresponds with a user
    userId: str

    # contacts (emails, phones, external ids)
    contacts: typing.List[Contact]

    address: Address

    remoteWorkAddress: Address

    # birthdate
    birthDate: str

    # start date of most recent hire
    startDate: str

    # end date of most recent hire
    endDate: str

    # path to full-sized profile image in storage
    imagePath: str

    # path to pronunciation of the person's name
    nameAudioPath: str

    # self-reported gender
    gender: str

    # self-reported ethnicity
    ethnicity: str

    fields: PersonFields

    # personal sensitivity preferences around specific fields
    sensitiveFields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # sort order
    sort: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    inviteOptions: OrgAccess

    # current status within the organization
    state: str

class Person(RequiredPerson, OptionalPerson):
    pass
