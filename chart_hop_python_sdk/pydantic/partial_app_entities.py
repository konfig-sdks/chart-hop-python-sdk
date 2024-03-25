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

from chart_hop_python_sdk.pydantic.field import Field
from chart_hop_python_sdk.pydantic.partial_app_entities_jobs import PartialAppEntitiesJobs
from chart_hop_python_sdk.pydantic.partial_app_entities_person_to_job_map import PartialAppEntitiesPersonToJobMap
from chart_hop_python_sdk.pydantic.partial_app_entities_persons import PartialAppEntitiesPersons

class PartialAppEntities(BaseModel):
    jobs: PartialAppEntitiesJobs = Field(alias='jobs')

    persons: PartialAppEntitiesPersons = Field(alias='persons')

    person_to_job_map: PartialAppEntitiesPersonToJobMap = Field(alias='personToJobMap')

    fields: typing.List[Field] = Field(alias='fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
