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

from chart_hop_python_sdk.pydantic.event_fields import EventFields

class Event(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # user id who caused the event
    user_id: str = Field(alias='userId')

    # type of event
    type: Literal["APP", "APPROVE", "COMBINE", "CREATE", "DELETE", "DONE", "ERROR", "EXPORT_CSV", "EXPORT_ORG_CHART", "GENERATE", "GEOIP", "INCOMING", "INSTALL", "INVITE", "INBOUND", "LOGIN", "MERGE", "OUTBOUND", "PREVIEW_AS", "READ", "READ_SENSITIVE", "READ_ATS", "READ_ATS_WEBHOOK", "READ_FULL_NAME", "READ_FUTURE_DATE", "READ_METADATA", "READ_COMP", "READ_BILLING", "READ_PENDING", "READ_PAYROLL", "READ_SENSITIVE_FILTERS", "REJECT", "REMIND", "REMOVE_PASSWORD", "REQUEST", "RESTORE", "RESUME", "REVOKE", "RUN", "RUN_ATS", "SECURITY", "SHOW_DASHBOARD_DAYS_AHEAD", "SHOW_OPEN_JOBS", "STEP", "SUBMIT", "SYNC", "TEST", "TOKEN", "UNINSTALL", "UPDATE", "UPDATE_PASSWORD", "UPLOAD_CSV", "WRITE", "VIEW_AS"] = Field(alias='type')

    # type of target entity
    entity_type: Literal["ACTION", "AGREEMENT", "APP", "APP_CONFIG", "APPROVAL_CHAIN", "APPROVAL_CHAIN_STAGE", "APPROVAL_REQUEST", "ASSESSMENT", "BUDGET_POOL", "BUNDLE", "CATEGORY", "CATEGORY_SORT", "CHANGE", "COMMENT", "COMP_BAND", "COMP_REVIEW", "CONTENT", "CUSTOMER", "DATA_VIEW", "EXCHANGE_RATE", "EMAIL_TEMPLATE", "FIELD", "FILE", "FORM", "FORM_DRAFT", "FORM_RESPONSE", "GEOCODE", "GROUP", "GUIDELINE", "JOB", "JOB_LEVEL", "MEDIA", "MESSAGE", "MULTIPLIER", "ORG", "ORG_CONFIG", "PERSON", "PROFILE_TAB", "POLICY", "POSITION", "PROCESS", "PRODUCT", "QUERY_TOKEN", "QUESTION", "REPORT", "REPORT_CHART", "ROLE", "SCENARIO", "STOCK_PRICE", "TABLE", "TABLE_ROW", "TASK_CONFIG", "TEMPLATE", "TASK", "TOKEN", "TIMEOFF", "TRACKED_GROUP", "USER"] = Field(alias='entityType')

    # id of target entity
    entity_id: str = Field(alias='entityId')

    # timestamp of event
    at: int = Field(alias='at')

    # parent organization id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # id of table, if entity is a table row
    table_id: typing.Optional[str] = Field(None, alias='tableId')

    # jobId of the entity, if the entity is a job or closely connected to a single job
    job_id: typing.Optional[str] = Field(None, alias='jobId')

    # personId of the entity, if the entity is a person or closely connected to a single person
    person_id: typing.Optional[str] = Field(None, alias='personId')

    # subtype of entity
    subtype: typing.Optional[str] = Field(None, alias='subtype')

    # event-specific payload containing information about the change that took place
    payload: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='payload')

    # id of process
    process_id: typing.Optional[str] = Field(None, alias='processId')

    # effective date, if in use
    date: typing.Optional[date] = Field(None, alias='date')

    # id of scenario
    scenario_id: typing.Optional[str] = Field(None, alias='scenarioId')

    # id of associated entity, such as comp cycle
    parent_entity_id: typing.Optional[str] = Field(None, alias='parentEntityId')

    fields: typing.Optional[EventFields] = Field(None, alias='fields')

    # event code, for example job.update
    code: typing.Optional[str] = Field(None, alias='code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
