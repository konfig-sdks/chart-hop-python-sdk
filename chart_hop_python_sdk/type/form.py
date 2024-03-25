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

from chart_hop_python_sdk.type.form_block import FormBlock
from chart_hop_python_sdk.type.form_field import FormField

class RequiredForm(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable full name of form
    label: str

    # ordered list of fields being collected in this form
    fields: typing.List[FormField]

    # status of the form
    status: str

    # options, such as notification settings
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalForm(TypedDict, total=False):
    # description of form
    description: str

    # ordered list of blocks being collected in this form
    blocks: typing.List[FormBlock]

    # type of the form
    type: str

    # target type that the form can be filled out about (null defaults to PERSON for backwards compatibility)
    targetType: str

    # filter that controls on which profiles this tab will appear
    targetFilter: str

    # filter that controls which respondents can submit this form. The form:submit permission, if present, overrides this filter
    submitFilter: str

    # filter that controls who can read the form responses. The formResponse:read permission, if present, overrides this filter
    responseReadFilter: str

    # if this option is on, then form response answers will use field permissions to determine access to those responses
    useFieldAccess: bool

    # approval needed, if any approval is required
    approval: str

    # view sensitivity for the author of this form - the level of view access required to view the createId and updateId fields. If null, the author's identity is always visible as long as the viewer can read the form response. If set to PRIVATE, the author's identity is stored in ChartHop, but protected such that even users with sensitive access cannot access the data. If set to ANONYMOUS, the author's identity is not stored in ChartHop at all.
    authorSensitive: str

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

class Form(RequiredForm, OptionalForm):
    pass
