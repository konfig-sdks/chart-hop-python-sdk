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


class RequiredGenerateTemplateRequest(TypedDict):
    saveToFiles: bool

    sendToManagers: bool

    sendToPersons: bool

    useScenarioChanges: bool

class OptionalGenerateTemplateRequest(TypedDict, total=False):
    filter: str

    emailSubject: str

    emailMessage: str

    fileSensitive: str

    fileField: str

    scenarioId: str

    date: date

    changeGroupingType: str

    changeGroupingId: str

class GenerateTemplateRequest(RequiredGenerateTemplateRequest, OptionalGenerateTemplateRequest):
    pass
