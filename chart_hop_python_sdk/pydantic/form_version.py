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

from chart_hop_python_sdk.pydantic.form import Form
from chart_hop_python_sdk.pydantic.question import Question

class FormVersion(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # form id
    form_id: str = Field(alias='formId')

    form: typing.Optional[Form] = Field(None, alias='form')

    # questions contained in form, at the time of version creation
    questions: typing.Optional[typing.List[Question]] = Field(None, alias='questions')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
