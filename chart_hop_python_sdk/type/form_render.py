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

from chart_hop_python_sdk.type.form_render_block import FormRenderBlock
from chart_hop_python_sdk.type.form_render_options import FormRenderOptions
from chart_hop_python_sdk.type.form_render_rerender_question_ids import FormRenderRerenderQuestionIds

class RequiredFormRender(TypedDict):
    id: str

    label: str

    options: FormRenderOptions

    blocks: typing.List[FormRenderBlock]

    rerenderQuestionIds: FormRenderRerenderQuestionIds

    responseSensitive: str

class OptionalFormRender(TypedDict, total=False):
    authorSensitive: str

class FormRender(RequiredFormRender, OptionalFormRender):
    pass
