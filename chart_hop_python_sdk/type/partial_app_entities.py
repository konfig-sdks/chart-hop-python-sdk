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

from chart_hop_python_sdk.type.field import Field
from chart_hop_python_sdk.type.partial_app_entities_jobs import PartialAppEntitiesJobs
from chart_hop_python_sdk.type.partial_app_entities_person_to_job_map import PartialAppEntitiesPersonToJobMap
from chart_hop_python_sdk.type.partial_app_entities_persons import PartialAppEntitiesPersons

class RequiredPartialAppEntities(TypedDict):
    jobs: PartialAppEntitiesJobs

    persons: PartialAppEntitiesPersons

    personToJobMap: PartialAppEntitiesPersonToJobMap

    fields: typing.List[Field]

class OptionalPartialAppEntities(TypedDict, total=False):
    pass

class PartialAppEntities(RequiredPartialAppEntities, OptionalPartialAppEntities):
    pass
