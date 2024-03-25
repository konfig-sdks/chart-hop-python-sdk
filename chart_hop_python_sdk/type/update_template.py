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

from chart_hop_python_sdk.type.update_template_tags import UpdateTemplateTags

class RequiredUpdateTemplate(TypedDict):
    pass

class OptionalUpdateTemplate(TypedDict, total=False):
    tags: UpdateTemplateTags

    # description of template
    description: str

    # template name, must be unique to organization
    name: str

    # template content
    content: str

    # template inline stylesheet
    stylesheet: str

    # type of template
    type: str

    # document filename CQL
    filename: str

class UpdateTemplate(RequiredUpdateTemplate, OptionalUpdateTemplate):
    pass
