# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from chart_hop_python_sdk import schemas  # noqa: F401


class UpdateOrgConfig(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def hiddenFieldIds() -> typing.Type['UpdateOrgConfigHiddenFieldIds']:
                return UpdateOrgConfigHiddenFieldIds
            
            
            class builtinCategoryMap(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BuiltInCategoryMap']:
                        return BuiltInCategoryMap
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BuiltInCategoryMap'], typing.List['BuiltInCategoryMap']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'builtinCategoryMap':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BuiltInCategoryMap':
                    return super().__getitem__(i)
            
            
            class builtinFieldConfig(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BuiltInFieldConfig']:
                        return BuiltInFieldConfig
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BuiltInFieldConfig'], typing.List['BuiltInFieldConfig']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'builtinFieldConfig':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BuiltInFieldConfig':
                    return super().__getitem__(i)
        
            @staticmethod
            def compensationBandsConfig() -> typing.Type['CompensationBandsConfig']:
                return CompensationBandsConfig
            
            
            class smartCurrencyOptions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SmartCurrencyOption']:
                        return SmartCurrencyOption
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SmartCurrencyOption'], typing.List['SmartCurrencyOption']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'smartCurrencyOptions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SmartCurrencyOption':
                    return super().__getitem__(i)
            smartCurrencyDefault = schemas.StrSchema
        
            @staticmethod
            def requiredJobFields() -> typing.Type['UpdateOrgConfigRequiredJobFields']:
                return UpdateOrgConfigRequiredJobFields
        
            @staticmethod
            def scenarioApprovalChains() -> typing.Type['UpdateOrgConfigScenarioApprovalChains']:
                return UpdateOrgConfigScenarioApprovalChains
            isOpenJobRoleApprovalEnabled = schemas.BoolSchema
            
            
            class grantConfiguration(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GrantAlias']:
                        return GrantAlias
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GrantAlias'], typing.List['GrantAlias']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'grantConfiguration':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GrantAlias':
                    return super().__getitem__(i)
            __annotations__ = {
                "hiddenFieldIds": hiddenFieldIds,
                "builtinCategoryMap": builtinCategoryMap,
                "builtinFieldConfig": builtinFieldConfig,
                "compensationBandsConfig": compensationBandsConfig,
                "smartCurrencyOptions": smartCurrencyOptions,
                "smartCurrencyDefault": smartCurrencyDefault,
                "requiredJobFields": requiredJobFields,
                "scenarioApprovalChains": scenarioApprovalChains,
                "isOpenJobRoleApprovalEnabled": isOpenJobRoleApprovalEnabled,
                "grantConfiguration": grantConfiguration,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hiddenFieldIds"]) -> 'UpdateOrgConfigHiddenFieldIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["builtinCategoryMap"]) -> MetaOapg.properties.builtinCategoryMap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["builtinFieldConfig"]) -> MetaOapg.properties.builtinFieldConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensationBandsConfig"]) -> 'CompensationBandsConfig': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smartCurrencyOptions"]) -> MetaOapg.properties.smartCurrencyOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smartCurrencyDefault"]) -> MetaOapg.properties.smartCurrencyDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requiredJobFields"]) -> 'UpdateOrgConfigRequiredJobFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenarioApprovalChains"]) -> 'UpdateOrgConfigScenarioApprovalChains': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isOpenJobRoleApprovalEnabled"]) -> MetaOapg.properties.isOpenJobRoleApprovalEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantConfiguration"]) -> MetaOapg.properties.grantConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hiddenFieldIds", "builtinCategoryMap", "builtinFieldConfig", "compensationBandsConfig", "smartCurrencyOptions", "smartCurrencyDefault", "requiredJobFields", "scenarioApprovalChains", "isOpenJobRoleApprovalEnabled", "grantConfiguration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hiddenFieldIds"]) -> typing.Union['UpdateOrgConfigHiddenFieldIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["builtinCategoryMap"]) -> typing.Union[MetaOapg.properties.builtinCategoryMap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["builtinFieldConfig"]) -> typing.Union[MetaOapg.properties.builtinFieldConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensationBandsConfig"]) -> typing.Union['CompensationBandsConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smartCurrencyOptions"]) -> typing.Union[MetaOapg.properties.smartCurrencyOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smartCurrencyDefault"]) -> typing.Union[MetaOapg.properties.smartCurrencyDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requiredJobFields"]) -> typing.Union['UpdateOrgConfigRequiredJobFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenarioApprovalChains"]) -> typing.Union['UpdateOrgConfigScenarioApprovalChains', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isOpenJobRoleApprovalEnabled"]) -> typing.Union[MetaOapg.properties.isOpenJobRoleApprovalEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantConfiguration"]) -> typing.Union[MetaOapg.properties.grantConfiguration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hiddenFieldIds", "builtinCategoryMap", "builtinFieldConfig", "compensationBandsConfig", "smartCurrencyOptions", "smartCurrencyDefault", "requiredJobFields", "scenarioApprovalChains", "isOpenJobRoleApprovalEnabled", "grantConfiguration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hiddenFieldIds: typing.Union['UpdateOrgConfigHiddenFieldIds', schemas.Unset] = schemas.unset,
        builtinCategoryMap: typing.Union[MetaOapg.properties.builtinCategoryMap, list, tuple, schemas.Unset] = schemas.unset,
        builtinFieldConfig: typing.Union[MetaOapg.properties.builtinFieldConfig, list, tuple, schemas.Unset] = schemas.unset,
        compensationBandsConfig: typing.Union['CompensationBandsConfig', schemas.Unset] = schemas.unset,
        smartCurrencyOptions: typing.Union[MetaOapg.properties.smartCurrencyOptions, list, tuple, schemas.Unset] = schemas.unset,
        smartCurrencyDefault: typing.Union[MetaOapg.properties.smartCurrencyDefault, str, schemas.Unset] = schemas.unset,
        requiredJobFields: typing.Union['UpdateOrgConfigRequiredJobFields', schemas.Unset] = schemas.unset,
        scenarioApprovalChains: typing.Union['UpdateOrgConfigScenarioApprovalChains', schemas.Unset] = schemas.unset,
        isOpenJobRoleApprovalEnabled: typing.Union[MetaOapg.properties.isOpenJobRoleApprovalEnabled, bool, schemas.Unset] = schemas.unset,
        grantConfiguration: typing.Union[MetaOapg.properties.grantConfiguration, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateOrgConfig':
        return super().__new__(
            cls,
            *args,
            hiddenFieldIds=hiddenFieldIds,
            builtinCategoryMap=builtinCategoryMap,
            builtinFieldConfig=builtinFieldConfig,
            compensationBandsConfig=compensationBandsConfig,
            smartCurrencyOptions=smartCurrencyOptions,
            smartCurrencyDefault=smartCurrencyDefault,
            requiredJobFields=requiredJobFields,
            scenarioApprovalChains=scenarioApprovalChains,
            isOpenJobRoleApprovalEnabled=isOpenJobRoleApprovalEnabled,
            grantConfiguration=grantConfiguration,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.built_in_category_map import BuiltInCategoryMap
from chart_hop_python_sdk.model.built_in_field_config import BuiltInFieldConfig
from chart_hop_python_sdk.model.compensation_bands_config import CompensationBandsConfig
from chart_hop_python_sdk.model.grant_alias import GrantAlias
from chart_hop_python_sdk.model.smart_currency_option import SmartCurrencyOption
from chart_hop_python_sdk.model.update_org_config_hidden_field_ids import UpdateOrgConfigHiddenFieldIds
from chart_hop_python_sdk.model.update_org_config_required_job_fields import UpdateOrgConfigRequiredJobFields
from chart_hop_python_sdk.model.update_org_config_scenario_approval_chains import UpdateOrgConfigScenarioApprovalChains
