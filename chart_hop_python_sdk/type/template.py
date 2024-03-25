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

from chart_hop_python_sdk.type.template_tags import TemplateTags

class RequiredTemplate(TypedDict):
    tags: TemplateTags

    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # template name, must be unique to organization
    name: str

    # template content
    content: str

    # template content format - must be MARKDOWN
    format: str

    # type of template
    type: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

class OptionalTemplate(TypedDict, total=False):
    # description of template
    description: str

    # template inline stylesheet
    stylesheet: str

    # document filename CQL
    filename: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class Template(RequiredTemplate, OptionalTemplate):
    pass
