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

from chart_hop_python_sdk.type.enum_value import EnumValue
from chart_hop_python_sdk.type.field_aliases import FieldAliases
from chart_hop_python_sdk.type.field_category_ids import FieldCategoryIds
from chart_hop_python_sdk.type.field_override_revert import FieldOverrideRevert
from chart_hop_python_sdk.type.table_ref import TableRef

class RequiredField(TypedDict):
    # globally unique id
    id: str

    # short field name
    name: str

    # human-readable full name of field
    label: str

    # type of field
    type: str

    # plural type of the field (either SINGLE, LIST, or SET)
    plural: str

    # indicates that this field value is unique in conjunction with entityType PERSON or JOB
    isUnique: bool

    # indicates that this field value is required
    isRequired: bool

    # sensitivity level of data
    sensitive: str

class OptionalField(TypedDict, total=False):
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

    # possible values (enum type only)
    values: typing.List[EnumValue]

    # default value if field is not set
    defaultValue: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # validation options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # entity type of field
    entityType: str

    # indicates that this field value is effective-dated
    isEffectiveDated: bool

    aliases: FieldAliases

    # unique ID for the function that runs to calculate the value of this field. For native fields only
    calc: str

    # indicates how this field is calculated (whether it's stored in the DB, evaluated through the expression service, or compound)
    classification: str

    # hide expression-derived values from non-sensitive users
    hideExpr: bool

    # number of days after which the data becomes invalid
    expireDays: int

    # the category the field belongs to
    categoryId: str

    categoryIds: FieldCategoryIds

    # the status of the field
    status: str

    # the table id this field applies to, only applicable when EntityType equals TABLE
    tableId: str

    tableName: str

    tableRef: TableRef

    readonly: bool

    builtIn: bool

    canOverrideSensitivity: bool

    # number of decimal places for money values
    places: int

    overrideRevert: FieldOverrideRevert

    overrideName: str

    hasSubfields: bool

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

class Field(RequiredField, OptionalField):
    pass
