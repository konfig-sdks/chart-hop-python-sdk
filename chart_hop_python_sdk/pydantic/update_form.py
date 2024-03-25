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

from chart_hop_python_sdk.pydantic.form_block import FormBlock
from chart_hop_python_sdk.pydantic.form_field import FormField

class UpdateForm(BaseModel):
    # description of form
    description: typing.Optional[str] = Field(None, alias='description')

    # human-readable full name of form
    label: typing.Optional[str] = Field(None, alias='label')

    # ordered list of fields being collected in this form
    fields: typing.Optional[typing.List[FormField]] = Field(None, alias='fields')

    # ordered list of blocks being collected in this form
    blocks: typing.Optional[typing.List[FormBlock]] = Field(None, alias='blocks')

    # status of the form
    status: typing.Optional[Literal["ACTIVE", "INACTIVE", "ARCHIVED"]] = Field(None, alias='status')

    # type of the form
    type: typing.Optional[Literal["BUILT_IN", "CUSTOM"]] = Field(None, alias='type')

    # target type that the form can be filled out about (null defaults to PERSON for backwards compatibility)
    target_type: typing.Optional[Literal["NONE", "PERSON"]] = Field(None, alias='targetType')

    # filter that controls on which profiles this tab will appear
    target_filter: typing.Optional[str] = Field(None, alias='targetFilter')

    # filter that controls which respondents can submit this form. The form:submit permission, if present, overrides this filter
    submit_filter: typing.Optional[str] = Field(None, alias='submitFilter')

    # filter that controls who can read the form responses. The formResponse:read permission, if present, overrides this filter
    response_read_filter: typing.Optional[str] = Field(None, alias='responseReadFilter')

    # if this option is on, then form response answers will use field permissions to determine access to those responses
    use_field_access: typing.Optional[bool] = Field(None, alias='useFieldAccess')

    # approval needed, if any approval is required
    approval: typing.Optional[Literal["MANAGER", "GRAND_MANAGER"]] = Field(None, alias='approval')

    # view sensitivity for the author of this form - the level of view access required to view the createId and updateId fields. If null, the author's identity is always visible as long as the viewer can read the form response. If set to PRIVATE, the author's identity is stored in ChartHop, but protected such that even users with sensitive access cannot access the data. If set to ANONYMOUS, the author's identity is not stored in ChartHop at all.
    author_sensitive: typing.Optional[Literal["ANONYMOUS", "PRIVATE", "HIGH", "MANAGER"]] = Field(None, alias='authorSensitive')

    # options, such as notification settings
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
