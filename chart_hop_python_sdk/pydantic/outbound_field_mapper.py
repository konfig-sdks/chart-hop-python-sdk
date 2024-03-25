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

from chart_hop_python_sdk.pydantic.outbound_value_mapper import OutboundValueMapper

class OutboundFieldMapper(BaseModel):
    description: str = Field(alias='description')

    namespace: str = Field(alias='namespace')

    value_mappers: typing.List[OutboundValueMapper] = Field(alias='valueMappers')

    id: typing.Optional[str] = Field(None, alias='id')

    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
