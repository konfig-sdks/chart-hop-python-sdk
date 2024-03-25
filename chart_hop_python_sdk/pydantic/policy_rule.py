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

from chart_hop_python_sdk.pydantic.policy_rule_allow import PolicyRuleAllow
from chart_hop_python_sdk.pydantic.policy_rule_categories import PolicyRuleCategories
from chart_hop_python_sdk.pydantic.policy_rule_deny import PolicyRuleDeny
from chart_hop_python_sdk.pydantic.policy_rule_department_ids import PolicyRuleDepartmentIds
from chart_hop_python_sdk.pydantic.policy_rule_directions import PolicyRuleDirections
from chart_hop_python_sdk.pydantic.policy_rule_fields import PolicyRuleFields
from chart_hop_python_sdk.pydantic.policy_rule_fields_sensitive import PolicyRuleFieldsSensitive
from chart_hop_python_sdk.pydantic.policy_rule_types import PolicyRuleTypes
from chart_hop_python_sdk.pydantic.policy_rule_visible_sensitive import PolicyRuleVisibleSensitive

class PolicyRule(BaseModel):
    allow: typing.Optional[PolicyRuleAllow] = Field(None, alias='allow')

    deny: typing.Optional[PolicyRuleDeny] = Field(None, alias='deny')

    categories: typing.Optional[PolicyRuleCategories] = Field(None, alias='categories')

    fields: typing.Optional[PolicyRuleFields] = Field(None, alias='fields')

    department_ids: typing.Optional[PolicyRuleDepartmentIds] = Field(None, alias='departmentIds')

    # custom filter the rule is limited to
    filter: typing.Optional[str] = Field(None, alias='filter')

    directions: typing.Optional[PolicyRuleDirections] = Field(None, alias='directions')

    types: typing.Optional[PolicyRuleTypes] = Field(None, alias='types')

    visible_sensitive: typing.Optional[PolicyRuleVisibleSensitive] = Field(None, alias='visibleSensitive')

    fields_sensitive: typing.Optional[PolicyRuleFieldsSensitive] = Field(None, alias='fieldsSensitive')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
