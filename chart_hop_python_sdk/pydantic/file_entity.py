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


class FileEntity(BaseModel):
    # globally unique id of file
    id: str = Field(alias='id')

    # customer facing filename of file
    filename: str = Field(alias='filename')

    # original filename of file
    original_filename: str = Field(alias='originalFilename')

    # mime type of file
    type: str = Field(alias='type')

    # extension of file
    ext: str = Field(alias='ext')

    # size of file in bytes
    bytes: int = Field(alias='bytes')

    # parent org id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # entity id that the file is attached to
    entity_id: typing.Optional[str] = Field(None, alias='entityId')

    # entity type (should only be PERSON or USER)
    entity_type: typing.Optional[Literal["ACTION", "AGREEMENT", "APP", "APP_CONFIG", "APPROVAL_CHAIN", "APPROVAL_CHAIN_STAGE", "APPROVAL_REQUEST", "ASSESSMENT", "BUDGET_POOL", "BUNDLE", "CATEGORY", "CATEGORY_SORT", "CHANGE", "COMMENT", "COMP_BAND", "COMP_REVIEW", "CONTENT", "CUSTOMER", "DATA_VIEW", "EXCHANGE_RATE", "EMAIL_TEMPLATE", "FIELD", "FILE", "FORM", "FORM_DRAFT", "FORM_RESPONSE", "GEOCODE", "GROUP", "GUIDELINE", "JOB", "JOB_LEVEL", "MEDIA", "MESSAGE", "MULTIPLIER", "ORG", "ORG_CONFIG", "PERSON", "PROFILE_TAB", "POLICY", "POSITION", "PROCESS", "PRODUCT", "QUERY_TOKEN", "QUESTION", "REPORT", "REPORT_CHART", "ROLE", "SCENARIO", "STOCK_PRICE", "TABLE", "TABLE_ROW", "TASK_CONFIG", "TEMPLATE", "TASK", "TOKEN", "TIMEOFF", "TRACKED_GROUP", "USER"]] = Field(None, alias='entityType')

    # field name that the file uses, if the file is tied to a field
    field: typing.Optional[str] = Field(None, alias='field')

    # level of sensitivity of the file, if the file is not tied to a field
    sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='sensitive')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
