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
from chart_hop_python_sdk.type.smart_currency_option import SmartCurrencyOption
from chart_hop_python_sdk.type.update_org_config_hidden_field_ids import UpdateOrgConfigHiddenFieldIds
from chart_hop_python_sdk.type.update_org_config_required_job_fields import UpdateOrgConfigRequiredJobFields
from chart_hop_python_sdk.type.update_org_config_scenario_approval_chains import UpdateOrgConfigScenarioApprovalChains

class RequiredUpdateOrgConfig(TypedDict):
    pass

class OptionalUpdateOrgConfig(TypedDict, total=False):
    hiddenFieldIds: UpdateOrgConfigHiddenFieldIds

    # set of maps of the custom fields that belongs to a built-in category
    builtinCategoryMap: typing.List[BuiltInCategoryMap]

    # Org configuration for built-in fields
    builtinFieldConfig: typing.List[BuiltInFieldConfig]

    compensationBandsConfig: CompensationBandsConfig

    # Options for where to source a currency to use when currency is unknown. order specific
    smartCurrencyOptions: typing.List[SmartCurrencyOption]

    # The default currency to use when currency is unknown and there are no options set in smartCurrencyOptions
    smartCurrencyDefault: str

    requiredJobFields: UpdateOrgConfigRequiredJobFields

    scenarioApprovalChains: UpdateOrgConfigScenarioApprovalChains

    # Whether to show open job approval on Open Job Profile page
    isOpenJobRoleApprovalEnabled: bool

    # Org Grant Configuration
    grantConfiguration: typing.List[GrantAlias]

class UpdateOrgConfig(RequiredUpdateOrgConfig, OptionalUpdateOrgConfig):
    pass
