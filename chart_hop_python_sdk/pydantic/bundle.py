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

from chart_hop_python_sdk.pydantic.bundle_report import BundleReport
from chart_hop_python_sdk.pydantic.category import Category
from chart_hop_python_sdk.pydantic.content import Content
from chart_hop_python_sdk.pydantic.partial_action import PartialAction
from chart_hop_python_sdk.pydantic.partial_field import PartialField
from chart_hop_python_sdk.pydantic.partial_form import PartialForm
from chart_hop_python_sdk.pydantic.partial_group import PartialGroup
from chart_hop_python_sdk.pydantic.partial_profile_tab import PartialProfileTab
from chart_hop_python_sdk.pydantic.partial_task_config import PartialTaskConfig
from chart_hop_python_sdk.pydantic.question import Question
from chart_hop_python_sdk.pydantic.template import Template

class Bundle(BaseModel):
    # list of categories included in this bundle
    categories: typing.Optional[typing.List[Category]] = Field(None, alias='categories')

    # list of fields included in this bundle
    fields: typing.Optional[typing.List[PartialField]] = Field(None, alias='fields')

    # list of forms included in this bundle
    forms: typing.Optional[typing.List[PartialForm]] = Field(None, alias='forms')

    # list of questions included in this bundle
    questions: typing.Optional[typing.List[Question]] = Field(None, alias='questions')

    # list of profile tabs included in this bundle
    profile_tabs: typing.Optional[typing.List[PartialProfileTab]] = Field(None, alias='profileTabs')

    # list of content groups included in this bundle
    groups: typing.Optional[typing.List[PartialGroup]] = Field(None, alias='groups')

    # list of reports included in this bundle
    reports: typing.Optional[typing.List[BundleReport]] = Field(None, alias='reports')

    # list of actions included in this bundle
    actions: typing.Optional[typing.List[PartialAction]] = Field(None, alias='actions')

    # list of templates included in this bundle
    templates: typing.Optional[typing.List[Template]] = Field(None, alias='templates')

    # list of resource content included in this bundle
    contents: typing.Optional[typing.List[Content]] = Field(None, alias='contents')

    # list of task configs included in this bundle
    task_configs: typing.Optional[typing.List[PartialTaskConfig]] = Field(None, alias='taskConfigs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
