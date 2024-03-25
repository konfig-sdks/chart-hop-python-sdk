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

from chart_hop_python_sdk.type.app_config_disabled_field_mappers import AppConfigDisabledFieldMappers
from chart_hop_python_sdk.type.app_config_enabled_outbound_field_mappers import AppConfigEnabledOutboundFieldMappers
from chart_hop_python_sdk.type.app_config_template_matchers import AppConfigTemplateMatchers
from chart_hop_python_sdk.type.field_mapper import FieldMapper
from chart_hop_python_sdk.type.outbound_field_mapper import OutboundFieldMapper

class RequiredAppConfig(TypedDict):
    # app id
    appId: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalAppConfig(TypedDict, total=False):
    # globally unique id
    id: str

    # user id, if this person corresponds with a user
    userId: str

    # org id, if this app config corresponds with an org
    orgId: str

    # list of default field mappers
    fieldMappers: typing.List[FieldMapper]

    # list of custom field mappers by a user
    customFieldMappers: typing.List[FieldMapper]

    # list of default outbound field mappers
    defaultOutboundFieldMappers: typing.List[OutboundFieldMapper]

    # list of custom outbound field mappers
    customOutboundFieldMappers: typing.List[OutboundFieldMapper]

    disabledFieldMappers: AppConfigDisabledFieldMappers

    enabledOutboundFieldMappers: AppConfigEnabledOutboundFieldMappers

    templateMatchers: AppConfigTemplateMatchers

    # app specific options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class AppConfig(RequiredAppConfig, OptionalAppConfig):
    pass
