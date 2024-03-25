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

from chart_hop_python_sdk.pydantic.app_config_disabled_field_mappers import AppConfigDisabledFieldMappers
from chart_hop_python_sdk.pydantic.app_config_enabled_outbound_field_mappers import AppConfigEnabledOutboundFieldMappers
from chart_hop_python_sdk.pydantic.app_config_template_matchers import AppConfigTemplateMatchers
from chart_hop_python_sdk.pydantic.field_mapper import FieldMapper
from chart_hop_python_sdk.pydantic.outbound_field_mapper import OutboundFieldMapper

class AppConfig(BaseModel):
    # app id
    app_id: str = Field(alias='appId')

    # created by user id
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # last updated by user id
    update_id: str = Field(alias='updateId')

    # last updated timestamp
    update_at: str = Field(alias='updateAt')

    # globally unique id
    id: typing.Optional[str] = Field(None, alias='id')

    # user id, if this person corresponds with a user
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # org id, if this app config corresponds with an org
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # list of default field mappers
    field_mappers: typing.Optional[typing.List[FieldMapper]] = Field(None, alias='fieldMappers')

    # list of custom field mappers by a user
    custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = Field(None, alias='customFieldMappers')

    # list of default outbound field mappers
    default_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = Field(None, alias='defaultOutboundFieldMappers')

    # list of custom outbound field mappers
    custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = Field(None, alias='customOutboundFieldMappers')

    disabled_field_mappers: typing.Optional[AppConfigDisabledFieldMappers] = Field(None, alias='disabledFieldMappers')

    enabled_outbound_field_mappers: typing.Optional[AppConfigEnabledOutboundFieldMappers] = Field(None, alias='enabledOutboundFieldMappers')

    template_matchers: typing.Optional[AppConfigTemplateMatchers] = Field(None, alias='templateMatchers')

    # app specific options
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )