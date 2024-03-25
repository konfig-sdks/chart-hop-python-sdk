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


class GenerateTemplateRequest(BaseModel):
    save_to_files: bool = Field(alias='saveToFiles')

    send_to_managers: bool = Field(alias='sendToManagers')

    send_to_persons: bool = Field(alias='sendToPersons')

    use_scenario_changes: bool = Field(alias='useScenarioChanges')

    filter: typing.Optional[str] = Field(None, alias='filter')

    email_subject: typing.Optional[str] = Field(None, alias='emailSubject')

    email_message: typing.Optional[str] = Field(None, alias='emailMessage')

    file_sensitive: typing.Optional[Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"]] = Field(None, alias='fileSensitive')

    file_field: typing.Optional[str] = Field(None, alias='fileField')

    scenario_id: typing.Optional[str] = Field(None, alias='scenarioId')

    date: typing.Optional[date] = Field(None, alias='date')

    change_grouping_type: typing.Optional[Literal["PRIMARY", "SCENARIO", "COMP_REVIEW"]] = Field(None, alias='changeGroupingType')

    change_grouping_id: typing.Optional[str] = Field(None, alias='changeGroupingId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
