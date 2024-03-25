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
from chart_hop_python_sdk.type.update_person_fields import UpdatePersonFields

class RequiredUpdatePerson(TypedDict):
    pass

class OptionalUpdatePerson(TypedDict, total=False):
    name: Name

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

    fields: UpdatePersonFields

    # personal sensitivity preferences around specific fields
    sensitiveFields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    inviteOptions: OrgAccess

    # current status within the organization
    state: str

class UpdatePerson(RequiredUpdatePerson, OptionalUpdatePerson):
    pass
