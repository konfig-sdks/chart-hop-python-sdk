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

from chart_hop_python_sdk.pydantic.built_in_category_map import BuiltInCategoryMap
from chart_hop_python_sdk.pydantic.built_in_field_config import BuiltInFieldConfig
from chart_hop_python_sdk.pydantic.compensation_bands_config import CompensationBandsConfig
from chart_hop_python_sdk.pydantic.create_org_config_hidden_field_ids import CreateOrgConfigHiddenFieldIds
from chart_hop_python_sdk.pydantic.create_org_config_required_job_fields import CreateOrgConfigRequiredJobFields
from chart_hop_python_sdk.pydantic.create_org_config_scenario_approval_chains import CreateOrgConfigScenarioApprovalChains
from chart_hop_python_sdk.pydantic.grant_alias import GrantAlias
from chart_hop_python_sdk.pydantic.smart_currency_option import SmartCurrencyOption

class CreateOrgConfig(BaseModel):
    # parent organization id
    org_id: str = Field(alias='orgId')

    hidden_field_ids: typing.Optional[CreateOrgConfigHiddenFieldIds] = Field(None, alias='hiddenFieldIds')

    # set of maps of the custom fields that belongs to a built-in category
    builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = Field(None, alias='builtinCategoryMap')

    # Org configuration for built-in fields
    builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = Field(None, alias='builtinFieldConfig')

    compensation_bands_config: typing.Optional[CompensationBandsConfig] = Field(None, alias='compensationBandsConfig')

    # Options for where to source a currency to use when currency is unknown. order specific
    smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = Field(None, alias='smartCurrencyOptions')

    # The default currency to use when currency is unknown and there are no options set in smartCurrencyOptions
    smart_currency_default: typing.Optional[str] = Field(None, alias='smartCurrencyDefault')

    required_job_fields: typing.Optional[CreateOrgConfigRequiredJobFields] = Field(None, alias='requiredJobFields')

    scenario_approval_chains: typing.Optional[CreateOrgConfigScenarioApprovalChains] = Field(None, alias='scenarioApprovalChains')

    # Whether to show open job approval on Open Job Profile page
    is_open_job_role_approval_enabled: typing.Optional[bool] = Field(None, alias='isOpenJobRoleApprovalEnabled')

    # Org Grant Configuration
    grant_configuration: typing.Optional[typing.List[GrantAlias]] = Field(None, alias='grantConfiguration')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
