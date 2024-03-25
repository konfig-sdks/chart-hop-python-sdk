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

from chart_hop_python_sdk.type.built_in_category_map import BuiltInCategoryMap
from chart_hop_python_sdk.type.built_in_field_config import BuiltInFieldConfig
from chart_hop_python_sdk.type.compensation_bands_config import CompensationBandsConfig
from chart_hop_python_sdk.type.grant_alias import GrantAlias
from chart_hop_python_sdk.type.org_config_hidden_field_ids import OrgConfigHiddenFieldIds
from chart_hop_python_sdk.type.org_config_required_job_fields import OrgConfigRequiredJobFields
from chart_hop_python_sdk.type.org_config_scenario_approval_chains import OrgConfigScenarioApprovalChains
from chart_hop_python_sdk.type.smart_currency_option import SmartCurrencyOption

class RequiredOrgConfig(TypedDict):
    # globally unique id
    id: str

class OptionalOrgConfig(TypedDict, total=False):
    # parent organization id
    orgId: str

    hiddenFieldIds: OrgConfigHiddenFieldIds

    # set of maps of the custom fields that belongs to a built-in category
    builtinCategoryMap: typing.List[BuiltInCategoryMap]

    # Org configuration for built-in fields
    builtinFieldConfig: typing.List[BuiltInFieldConfig]

    compensationBandsConfig: CompensationBandsConfig

    # Options for where to source a currency to use when currency is unknown. order specific
    smartCurrencyOptions: typing.List[SmartCurrencyOption]

    # The default currency to use when currency is unknown and there are no options set in smartCurrencyOptions
    smartCurrencyDefault: str

    requiredJobFields: OrgConfigRequiredJobFields

    scenarioApprovalChains: OrgConfigScenarioApprovalChains

    # Whether to show open job approval on Open Job Profile page
    isOpenJobRoleApprovalEnabled: bool

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

    # Org Grant Configuration
    grantConfiguration: typing.List[GrantAlias]

class OrgConfig(RequiredOrgConfig, OptionalOrgConfig):
    pass
