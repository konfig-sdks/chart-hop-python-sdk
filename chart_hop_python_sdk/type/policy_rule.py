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

from chart_hop_python_sdk.type.policy_rule_allow import PolicyRuleAllow
from chart_hop_python_sdk.type.policy_rule_categories import PolicyRuleCategories
from chart_hop_python_sdk.type.policy_rule_deny import PolicyRuleDeny
from chart_hop_python_sdk.type.policy_rule_department_ids import PolicyRuleDepartmentIds
from chart_hop_python_sdk.type.policy_rule_directions import PolicyRuleDirections
from chart_hop_python_sdk.type.policy_rule_fields import PolicyRuleFields
from chart_hop_python_sdk.type.policy_rule_fields_sensitive import PolicyRuleFieldsSensitive
from chart_hop_python_sdk.type.policy_rule_types import PolicyRuleTypes
from chart_hop_python_sdk.type.policy_rule_visible_sensitive import PolicyRuleVisibleSensitive

class RequiredPolicyRule(TypedDict):
    pass

class OptionalPolicyRule(TypedDict, total=False):
    allow: PolicyRuleAllow

    deny: PolicyRuleDeny

    categories: PolicyRuleCategories

    fields: PolicyRuleFields

    departmentIds: PolicyRuleDepartmentIds

    # custom filter the rule is limited to
    filter: str

    directions: PolicyRuleDirections

    types: PolicyRuleTypes

    visibleSensitive: PolicyRuleVisibleSensitive

    fieldsSensitive: PolicyRuleFieldsSensitive

class PolicyRule(RequiredPolicyRule, OptionalPolicyRule):
    pass
