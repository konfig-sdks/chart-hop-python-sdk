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

from chart_hop_python_sdk.pydantic.form_render_block import FormRenderBlock
from chart_hop_python_sdk.pydantic.form_render_options import FormRenderOptions
from chart_hop_python_sdk.pydantic.form_render_rerender_question_ids import FormRenderRerenderQuestionIds

class FormRender(BaseModel):
    id: str = Field(alias='id')

    label: str = Field(alias='label')

    options: FormRenderOptions = Field(alias='options')

    blocks: typing.List[FormRenderBlock] = Field(alias='blocks')

    rerender_question_ids: FormRenderRerenderQuestionIds = Field(alias='rerenderQuestionIds')

    response_sensitive: Literal["GLOBAL", "ORG", "ORG_OTHER", "PERSONAL_DEMOG", "PERSONAL_BIRTH", "PERSONAL_CONTACT", "PERSONAL_PRIVATE", "SENSITIVE_BIRTH", "SENSITIVE_CONTACT", "TIMEOFF", "COMP_CASH", "COMP_EQUITY", "SENSITIVE", "PERSONAL", "MANAGER", "GRAND_MANAGER", "DIRECT", "PEERS", "HIGH", "PRIVATE"] = Field(alias='responseSensitive')

    author_sensitive: typing.Optional[Literal["ANONYMOUS", "PRIVATE", "HIGH", "MANAGER"]] = Field(None, alias='authorSensitive')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
