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

from chart_hop_python_sdk.type.bundle_report import BundleReport
from chart_hop_python_sdk.type.category import Category
from chart_hop_python_sdk.type.content import Content
from chart_hop_python_sdk.type.partial_action import PartialAction
from chart_hop_python_sdk.type.partial_field import PartialField
from chart_hop_python_sdk.type.partial_form import PartialForm
from chart_hop_python_sdk.type.partial_group import PartialGroup
from chart_hop_python_sdk.type.partial_profile_tab import PartialProfileTab
from chart_hop_python_sdk.type.partial_task_config import PartialTaskConfig
from chart_hop_python_sdk.type.question import Question
from chart_hop_python_sdk.type.template import Template

class RequiredBundle(TypedDict):
    pass

class OptionalBundle(TypedDict, total=False):
    # list of categories included in this bundle
    categories: typing.List[Category]

    # list of fields included in this bundle
    fields: typing.List[PartialField]

    # list of forms included in this bundle
    forms: typing.List[PartialForm]

    # list of questions included in this bundle
    questions: typing.List[Question]

    # list of profile tabs included in this bundle
    profileTabs: typing.List[PartialProfileTab]

    # list of content groups included in this bundle
    groups: typing.List[PartialGroup]

    # list of reports included in this bundle
    reports: typing.List[BundleReport]

    # list of actions included in this bundle
    actions: typing.List[PartialAction]

    # list of templates included in this bundle
    templates: typing.List[Template]

    # list of resource content included in this bundle
    contents: typing.List[Content]

    # list of task configs included in this bundle
    taskConfigs: typing.List[PartialTaskConfig]

class Bundle(RequiredBundle, OptionalBundle):
    pass
