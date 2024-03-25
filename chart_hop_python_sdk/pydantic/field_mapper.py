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

from chart_hop_python_sdk.pydantic.field_mapper_charthop_fields import FieldMapperCharthopFields
from chart_hop_python_sdk.pydantic.field_mapper_charthop_to_remote_map import FieldMapperCharthopToRemoteMap
from chart_hop_python_sdk.pydantic.field_mapper_map import FieldMapperMap
from chart_hop_python_sdk.pydantic.field_mapper_remote_fields import FieldMapperRemoteFields

class FieldMapper(BaseModel):
    charthop_fields: FieldMapperCharthopFields = Field(alias='charthopFields')

    remote_fields: FieldMapperRemoteFields = Field(alias='remoteFields')

    # type of field mapper to apply for mapping remote fields to ChartHop fields
    type: str = Field(alias='type')

    # unique id
    id: typing.Optional[str] = Field(None, alias='id')

    # default charthop value
    default_charthop_value: typing.Optional[str] = Field(None, alias='defaultCharthopValue')

    # default remote value
    default_remote_value: typing.Optional[str] = Field(None, alias='defaultRemoteValue')

    # default amount
    default_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='defaultAmount')

    # default currency
    default_currency: typing.Optional[str] = Field(None, alias='defaultCurrency')

    # transform function
    transform_function: typing.Optional[str] = Field(None, alias='transformFunction')

    # charthop to remote transform function
    charthop_to_remote_transform_function: typing.Optional[str] = Field(None, alias='charthopToRemoteTransformFunction')

    map: typing.Optional[FieldMapperMap] = Field(None, alias='map')

    charthop_to_remote_map: typing.Optional[FieldMapperCharthopToRemoteMap] = Field(None, alias='charthopToRemoteMap')

    # id field
    id_field: typing.Optional[str] = Field(None, alias='idField')

    # name field
    name_field: typing.Optional[str] = Field(None, alias='nameField')

    # remote to Charthop Multiplier
    remote_to_charthop_multiplier: typing.Optional[typing.Union[int, float]] = Field(None, alias='remoteToCharthopMultiplier')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
