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

from chart_hop_python_sdk.type.field_mapper import FieldMapper
from chart_hop_python_sdk.type.outbound_field_mapper import OutboundFieldMapper
from chart_hop_python_sdk.type.update_app_config_disabled_field_mappers import UpdateAppConfigDisabledFieldMappers
from chart_hop_python_sdk.type.update_app_config_enabled_outbound_field_mappers import UpdateAppConfigEnabledOutboundFieldMappers
from chart_hop_python_sdk.type.update_app_config_template_matchers import UpdateAppConfigTemplateMatchers

class RequiredUpdateAppConfig(TypedDict):
    pass

class OptionalUpdateAppConfig(TypedDict, total=False):
    # list of default field mappers
    fieldMappers: typing.List[FieldMapper]

    # list of custom field mappers by a user
    customFieldMappers: typing.List[FieldMapper]

    # list of custom outbound field mappers
    customOutboundFieldMappers: typing.List[OutboundFieldMapper]

    disabledFieldMappers: UpdateAppConfigDisabledFieldMappers

    enabledOutboundFieldMappers: UpdateAppConfigEnabledOutboundFieldMappers

    templateMatchers: UpdateAppConfigTemplateMatchers

    # app specific options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class UpdateAppConfig(RequiredUpdateAppConfig, OptionalUpdateAppConfig):
    pass
