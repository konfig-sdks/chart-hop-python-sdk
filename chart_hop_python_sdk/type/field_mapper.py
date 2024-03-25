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

from chart_hop_python_sdk.type.field_mapper_charthop_fields import FieldMapperCharthopFields
from chart_hop_python_sdk.type.field_mapper_charthop_to_remote_map import FieldMapperCharthopToRemoteMap
from chart_hop_python_sdk.type.field_mapper_map import FieldMapperMap
from chart_hop_python_sdk.type.field_mapper_remote_fields import FieldMapperRemoteFields

class RequiredFieldMapper(TypedDict):
    charthopFields: FieldMapperCharthopFields

    remoteFields: FieldMapperRemoteFields

    # type of field mapper to apply for mapping remote fields to ChartHop fields
    type: str

class OptionalFieldMapper(TypedDict, total=False):
    # unique id
    id: str

    # default charthop value
    defaultCharthopValue: str

    # default remote value
    defaultRemoteValue: str

    # default amount
    defaultAmount: typing.Union[int, float]

    # default currency
    defaultCurrency: str

    # transform function
    transformFunction: str

    # charthop to remote transform function
    charthopToRemoteTransformFunction: str

    map: FieldMapperMap

    charthopToRemoteMap: FieldMapperCharthopToRemoteMap

    # id field
    idField: str

    # name field
    nameField: str

    # remote to Charthop Multiplier
    remoteToCharthopMultiplier: typing.Union[int, float]

class FieldMapper(RequiredFieldMapper, OptionalFieldMapper):
    pass
