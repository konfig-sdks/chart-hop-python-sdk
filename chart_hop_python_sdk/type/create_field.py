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

from chart_hop_python_sdk.type.create_field_aliases import CreateFieldAliases
from chart_hop_python_sdk.type.create_field_data_fetch_types import CreateFieldDataFetchTypes
from chart_hop_python_sdk.type.enum_value import EnumValue
from chart_hop_python_sdk.type.table_ref import TableRef

class RequiredCreateField(TypedDict):
    # short field name
    name: str

    # human-readable full name of field
    label: str

    # type of field
    type: str

    # entity type of field
    entityType: str

    # sensitivity level of data
    sensitive: str

    # indicates that this field value is unique in conjunction with entityType PERSON or JOB
    isUnique: bool

    # indicates that this field value is required
    isRequired: bool

class OptionalCreateField(TypedDict, total=False):
    # description of field
    description: str

    # parent organization id (empty if global)
    orgId: str

    # human-readable question associated with field
    question: str

    # disallow any updates to this Field (except for field.question string)
    inUse: bool

    # calculated expression
    expr: str

    # the expected type of the evaluated expression
    exprType: str

    # plural type of the field (either SINGLE, LIST, or SET)
    plural: str

    # possible values (enum type only)
    values: typing.List[EnumValue]

    # default value if field is not set
    defaultValue: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # validation options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # hide expression-derived values from non-sensitive users
    hideExpr: bool

    # number of days after which the data becomes invalid
    expireDays: int

    # the status of the field
    status: str

    # the table id this field applies to, only applicable when EntityType equals TABLE
    tableId: str

    tableRef: TableRef

    # indicates that this field value is effective-dated
    isEffectiveDated: bool

    dataFetchTypes: CreateFieldDataFetchTypes

    aliases: CreateFieldAliases

    # unique ID for the function that runs to calculate the value of this field. For native fields only
    calc: str

    # ID of the category to which this field belongs, if any
    categoryId: str

    # indicates how this field is calculated (whether it's stored in the DB, evaluated through the expression service, or compound)
    classification: str

    # number of decimal places for money values
    places: int

class CreateField(RequiredCreateField, OptionalCreateField):
    pass
