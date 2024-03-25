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

from chart_hop_python_sdk.pydantic.create_field_aliases import CreateFieldAliases
from chart_hop_python_sdk.pydantic.create_field_data_fetch_types import CreateFieldDataFetchTypes
from chart_hop_python_sdk.pydantic.enum_value import EnumValue
from chart_hop_python_sdk.pydantic.table_ref import TableRef

class CreateField(BaseModel):
    # short field name
    name: str = Field(alias='name')

    # human-readable full name of field
    label: str = Field(alias='label')

    # type of field
    type: Literal["ADDRESS", "BOOLEAN", "COMP", "COMPOUND", "COMP_BAND", "CONTACTS", "CURRENCY", "DATE", "DECIMAL", "ELAPSED_DAYS", "ELAPSED_MONTHS", "ELAPSED_YEARS", "EMAIL", "ENUM", "ENUM_EXPR", "ENUM_MULTI", "ENUM_SCALE", "EXPR", "FILE", "GROUP", "GROUPS", "GROUP_ASSIGNMENTS", "GROUP_TYPE", "IMAGE", "INTEGER", "JOB", "JOBS", "JOB_TIER", "LIST", "MONEY", "NAME", "OBJECT", "PAY_INTERVAL", "PERCENT", "PERSON", "PERSONS", "PHONE", "STOCKGRANT", "STRING", "TABLE_REF", "TEXT", "TIMEOFF", "TIMESTAMP", "TRACKED_GROUP", "URL", "USER", "VARIABLE_COMP", "VARIABLE_COMPS"] = Field(alias='type')

    # entity type of field
    entity_type: Literal["JOB", "JOB_OPEN", "JOB_FILLED", "PERSON", "CHANGE", "TABLE", "ORG", "USER", "NONE"] = Field(alias='entityType')

    # sensitivity level of data
    sensitive: Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"] = Field(alias='sensitive')

    # indicates that this field value is unique in conjunction with entityType PERSON or JOB
    is_unique: bool = Field(alias='isUnique')

    # indicates that this field value is required
    is_required: bool = Field(alias='isRequired')

    # description of field
    description: typing.Optional[str] = Field(None, alias='description')

    # parent organization id (empty if global)
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # human-readable question associated with field
    question: typing.Optional[str] = Field(None, alias='question')

    # disallow any updates to this Field (except for field.question string)
    in_use: typing.Optional[bool] = Field(None, alias='inUse')

    # calculated expression
    expr: typing.Optional[str] = Field(None, alias='expr')

    # the expected type of the evaluated expression
    expr_type: typing.Optional[Literal["ADDRESS", "BOOLEAN", "COMP", "COMPOUND", "COMP_BAND", "CONTACTS", "CURRENCY", "DATE", "DECIMAL", "ELAPSED_DAYS", "ELAPSED_MONTHS", "ELAPSED_YEARS", "EMAIL", "ENUM", "ENUM_EXPR", "ENUM_MULTI", "ENUM_SCALE", "EXPR", "FILE", "GROUP", "GROUPS", "GROUP_ASSIGNMENTS", "GROUP_TYPE", "IMAGE", "INTEGER", "JOB", "JOBS", "JOB_TIER", "LIST", "MONEY", "NAME", "OBJECT", "PAY_INTERVAL", "PERCENT", "PERSON", "PERSONS", "PHONE", "STOCKGRANT", "STRING", "TABLE_REF", "TEXT", "TIMEOFF", "TIMESTAMP", "TRACKED_GROUP", "URL", "USER", "VARIABLE_COMP", "VARIABLE_COMPS"]] = Field(None, alias='exprType')

    # plural type of the field (either SINGLE, LIST, or SET)
    plural: typing.Optional[Literal["SINGLE", "LIST", "SET"]] = Field(None, alias='plural')

    # possible values (enum type only)
    values: typing.Optional[typing.List[EnumValue]] = Field(None, alias='values')

    # default value if field is not set
    default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='defaultValue')

    # validation options
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    # hide expression-derived values from non-sensitive users
    hide_expr: typing.Optional[bool] = Field(None, alias='hideExpr')

    # number of days after which the data becomes invalid
    expire_days: typing.Optional[int] = Field(None, alias='expireDays')

    # the status of the field
    status: typing.Optional[Literal["ACTIVE", "HIDDEN"]] = Field(None, alias='status')

    # the table id this field applies to, only applicable when EntityType equals TABLE
    table_id: typing.Optional[str] = Field(None, alias='tableId')

    table_ref: typing.Optional[TableRef] = Field(None, alias='tableRef')

    # indicates that this field value is effective-dated
    is_effective_dated: typing.Optional[bool] = Field(None, alias='isEffectiveDated')

    data_fetch_types: typing.Optional[CreateFieldDataFetchTypes] = Field(None, alias='dataFetchTypes')

    aliases: typing.Optional[CreateFieldAliases] = Field(None, alias='aliases')

    # unique ID for the function that runs to calculate the value of this field. For native fields only
    calc: typing.Optional[Literal["ADDRESS", "AGE", "ANNIVERSARY", "ANNUAL_BASE_MONEY", "BACKFILL", "BAND", "BAND_RANGE", "BASE", "BASE_CAL_YEAR_PRORATED", "BASE_CAL_YTD", "BASE_COMP", "BASE_COMP_AMOUNT", "BASE_COMP_ANNUALIZED", "BASE_COMP_ANNUALIZED_AS_ORG_CURRENCY", "BASE_COMP_AS_ORG_CURRENCY", "BASE_COMP_CHANGES", "BASE_COMP_CURRENCY", "BASE_COMP_HOURS_PER_WEEK", "BASE_COMP_INTERVAL", "BASE_COMP_LAST_RAISE_DATE", "BASE_COMP_LAST_RAISE_MONTHS_SINCE", "BASE_COMP_LAST_RAISE_PAY", "BASE_COMP_LAST_RAISE_PAY_AS_ORG_CURRENCY", "BASE_COMP_LAST_RAISE_PERCENT", "BASE_COMP_LAST_RAISE_TYPE", "BASE_COMP_PAY", "BASE_COMP_PAY_AS_ORG_CURRENCY", "BASE_COMP_WEEKS_PER_YEAR", "BASE_FISCAL_YEAR_PRORATED", "BASE_FISCAL_YTD", "BASE_PRIMARY", "BASE_RAISE_AMOUNT", "BASE_RAISE_DATE", "BASE_RAISE_PERCENT", "BIRTH_DATE", "BIRTHDAY", "BONUS_TARGET", "BUDGET_COST", "BUSINESS_UNITS", "CAL_YEAR_VEST_SHARES", "CAL_YEAR_VEST_VALUE", "CAN_APPROVE_CHANGE", "CAN_EDIT_JOB", "CASH_COMP", "CASH_COMP_LOCAL", "CHANGE", "CHANGE_ID", "COMMISSION_TARGET", "COMP", "COMP_CHANGE_PERCENT", "COMPA_RATIO_MID", "COMPA_RATIO_TARGET", "CONTACT", "COST", "CREATE_DATE", "CURRENCY", "DATA", "DATE", "DATE_OF", "DAYS_ACTIVE", "DAYS_OFF", "DAYS_OFF_TAKEN", "DAYS_OFF_UPCOMING", "DAYS_OPEN", "DB", "DEPART", "DEPARTMENT", "DEPARTMENT_FUNC", "DIRECT_JOBS", "DIRECT_JOB_COUNT", "DIRECT_PERSON_COUNT", "EMPLOYMENT", "END_DATE_JOB", "END_DATE_ORG", "ETHNICITY", "FISCAL_YEAR_COST", "GENDER", "GEOIP", "GEOIP_ADDRESS", "GRAND_MANAGER", "GRANT_SHARES", "GRANT_TYPE", "GRANT_VALUE", "GRANTS", "GROUP_IDS", "HEADCOUNT", "HISTORIC_BACKFILL", "HOUR", "HOURLY", "HOURLY_PRIMARY", "HOURS_PER_WEEK", "IMAGE", "INDIRECT", "INDIRECT_JOBS", "JOB", "JOB_ID", "JOB_CODE", "JOBCOUNT", "LAST_GRANT", "LAST_GRANT_DATE", "LAST_GRANT_ORIGINAL_VALUE", "LOCATION", "MANAGE_JOBS", "MANAGE_PERSONS", "MANAGER", "MANAGER_COUNT", "MANAGER_FILLED", "MANAGER_ID", "MANAGERS", "MANAGER_PERSON", "MANAGER_PERSONS", "ME", "MERGE_SCENARIO_ID", "NAME", "NAME_AUDIO", "NAME_TITLE", "NEXT_DAY_OFF", "NEXT_TIME_OFF", "NEXT_YEAR_VEST_SHARES", "NEXT_YEAR_VEST_VALUE", "NOTE", "NOOP", "OPEN", "ORG", "PERSON", "PERSON_ID", "PLACEMENT", "PREV_DAY_OFF", "PREV_TIME_OFF", "PROMOTION", "PROMOTION_DATE", "PROPOSED", "Q", "RAISE_AMOUNT", "RAISE_DATE", "RAISE_PERCENT", "RAISE_PROMOTION_DATE", "REASON", "REGRET", "RELATIONSHIPS", "REMOTE_WORK_ADDRESS", "SCENARIO", "SCENARIO_CHANGED", "SENSITIVE", "SENSITIVE_FIELDS", "START_DATE", "START_DATE_JOB", "START_DATE_ORG", "START_DATE_PLANNED", "STATE", "STRIKE_PRICE", "TARGET_HOURS_PER_WEEK", "TARGET_WEEKS_PER_YEAR", "TEAM", "TENURE_JOB", "TENURE_ORG", "TIMEZONE_OFFSET", "TITLE", "TITLE_DATE", "TODAY", "TOTAL_COMP", "TOTAL_COMP_LOCAL", "TOTAL_ORG_SHARES", "TOTAL_SHARES", "TOTAL_SHARES_VALUE", "UNDER", "UNDER_INCLUDING", "UNDER_JOBS", "UNVESTED_SHARES", "UNVESTED_VALUE", "UPDATE", "USER_ACTIVE_DAYS", "USER_CAN_EDIT_COMP_FOR_JOB", "USER", "VARIABLE", "VARIABLE_AMOUNT", "VARIABLE_INTERVAL", "VARIABLE_PERCENT", "VARIABLE_PRIMARY", "VARIABLE_TARGET", "VARIABLE_TARGET_AMOUNT", "VARIABLE_TARGET_ANNUALIZED", "VARIABLE_TARGET_CURRENCY", "VARIABLE_TARGET_PERCENT", "VARIABLE_TARGET_TYPE", "VARIABLE_TARGETS", "VARIABLE_TARGETS_LAST_RAISE_DATE", "VARIABLE_TARGETS_LAST_RAISE_MONTHS_SINCE", "VARIABLE_TARGETS_LAST_RAISE_PAY", "VARIABLE_TARGETS_LAST_RAISE_PERCENT", "VARIABLE_TYPE", "VESTED_DATE", "VESTED_SHARES", "VESTED_VALUE", "WEEKS_PER_YEAR", "WORK_ADDRESS"]] = Field(None, alias='calc')

    # ID of the category to which this field belongs, if any
    category_id: typing.Optional[str] = Field(None, alias='categoryId')

    # indicates how this field is calculated (whether it's stored in the DB, evaluated through the expression service, or compound)
    classification: typing.Optional[Literal["COMPOUND"]] = Field(None, alias='classification')

    # number of decimal places for money values
    places: typing.Optional[int] = Field(None, alias='places')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
