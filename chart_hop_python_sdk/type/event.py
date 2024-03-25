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

from chart_hop_python_sdk.type.event_fields import EventFields

class RequiredEvent(TypedDict):
    # globally unique id
    id: str

    # user id who caused the event
    userId: str

    # type of event
    type: str

    # type of target entity
    entityType: str

    # id of target entity
    entityId: str

    # timestamp of event
    at: int

class OptionalEvent(TypedDict, total=False):
    # parent organization id
    orgId: str

    # id of table, if entity is a table row
    tableId: str

    # jobId of the entity, if the entity is a job or closely connected to a single job
    jobId: str

    # personId of the entity, if the entity is a person or closely connected to a single person
    personId: str

    # subtype of entity
    subtype: str

    # event-specific payload containing information about the change that took place
    payload: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # id of process
    processId: str

    # effective date, if in use
    date: date

    # id of scenario
    scenarioId: str

    # id of associated entity, such as comp cycle
    parentEntityId: str

    fields: EventFields

    # event code, for example job.update
    code: str

class Event(RequiredEvent, OptionalEvent):
    pass
