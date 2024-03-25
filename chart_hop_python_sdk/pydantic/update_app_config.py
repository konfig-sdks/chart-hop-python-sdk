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

from chart_hop_python_sdk.pydantic.field_mapper import FieldMapper
from chart_hop_python_sdk.pydantic.outbound_field_mapper import OutboundFieldMapper
from chart_hop_python_sdk.pydantic.update_app_config_disabled_field_mappers import UpdateAppConfigDisabledFieldMappers
from chart_hop_python_sdk.pydantic.update_app_config_enabled_outbound_field_mappers import UpdateAppConfigEnabledOutboundFieldMappers
from chart_hop_python_sdk.pydantic.update_app_config_template_matchers import UpdateAppConfigTemplateMatchers

class UpdateAppConfig(BaseModel):
    # list of default field mappers
    field_mappers: typing.Optional[typing.List[FieldMapper]] = Field(None, alias='fieldMappers')

    # list of custom field mappers by a user
    custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = Field(None, alias='customFieldMappers')

    # list of custom outbound field mappers
    custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = Field(None, alias='customOutboundFieldMappers')

    disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = Field(None, alias='disabledFieldMappers')

    enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = Field(None, alias='enabledOutboundFieldMappers')

    template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = Field(None, alias='templateMatchers')

    # app specific options
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
