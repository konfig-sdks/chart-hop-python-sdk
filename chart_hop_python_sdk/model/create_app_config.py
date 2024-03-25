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


class CreateAppConfig(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "appId",
        }
        
        class properties:
            appId = schemas.StrSchema
            userId = schemas.StrSchema
            orgId = schemas.StrSchema
            
            
            class fieldMappers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FieldMapper']:
                        return FieldMapper
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FieldMapper'], typing.List['FieldMapper']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fieldMappers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FieldMapper':
                    return super().__getitem__(i)
            
            
            class customFieldMappers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FieldMapper']:
                        return FieldMapper
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FieldMapper'], typing.List['FieldMapper']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customFieldMappers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FieldMapper':
                    return super().__getitem__(i)
            
            
            class customOutboundFieldMappers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OutboundFieldMapper']:
                        return OutboundFieldMapper
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OutboundFieldMapper'], typing.List['OutboundFieldMapper']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customOutboundFieldMappers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OutboundFieldMapper':
                    return super().__getitem__(i)
        
            @staticmethod
            def disabledFieldMappers() -> typing.Type['CreateAppConfigDisabledFieldMappers']:
                return CreateAppConfigDisabledFieldMappers
        
            @staticmethod
            def enabledOutboundFieldMappers() -> typing.Type['CreateAppConfigEnabledOutboundFieldMappers']:
                return CreateAppConfigEnabledOutboundFieldMappers
        
            @staticmethod
            def templateMatchers() -> typing.Type['CreateAppConfigTemplateMatchers']:
                return CreateAppConfigTemplateMatchers
            options = schemas.DictSchema
            __annotations__ = {
                "appId": appId,
                "userId": userId,
                "orgId": orgId,
                "fieldMappers": fieldMappers,
                "customFieldMappers": customFieldMappers,
                "customOutboundFieldMappers": customOutboundFieldMappers,
                "disabledFieldMappers": disabledFieldMappers,
                "enabledOutboundFieldMappers": enabledOutboundFieldMappers,
                "templateMatchers": templateMatchers,
                "options": options,
            }
    
    appId: MetaOapg.properties.appId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldMappers"]) -> MetaOapg.properties.fieldMappers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldMappers"]) -> MetaOapg.properties.customFieldMappers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customOutboundFieldMappers"]) -> MetaOapg.properties.customOutboundFieldMappers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disabledFieldMappers"]) -> 'CreateAppConfigDisabledFieldMappers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledOutboundFieldMappers"]) -> 'CreateAppConfigEnabledOutboundFieldMappers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateMatchers"]) -> 'CreateAppConfigTemplateMatchers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appId", "userId", "orgId", "fieldMappers", "customFieldMappers", "customOutboundFieldMappers", "disabledFieldMappers", "enabledOutboundFieldMappers", "templateMatchers", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldMappers"]) -> typing.Union[MetaOapg.properties.fieldMappers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldMappers"]) -> typing.Union[MetaOapg.properties.customFieldMappers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customOutboundFieldMappers"]) -> typing.Union[MetaOapg.properties.customOutboundFieldMappers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disabledFieldMappers"]) -> typing.Union['CreateAppConfigDisabledFieldMappers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledOutboundFieldMappers"]) -> typing.Union['CreateAppConfigEnabledOutboundFieldMappers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateMatchers"]) -> typing.Union['CreateAppConfigTemplateMatchers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appId", "userId", "orgId", "fieldMappers", "customFieldMappers", "customOutboundFieldMappers", "disabledFieldMappers", "enabledOutboundFieldMappers", "templateMatchers", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        appId: typing.Union[MetaOapg.properties.appId, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        fieldMappers: typing.Union[MetaOapg.properties.fieldMappers, list, tuple, schemas.Unset] = schemas.unset,
        customFieldMappers: typing.Union[MetaOapg.properties.customFieldMappers, list, tuple, schemas.Unset] = schemas.unset,
        customOutboundFieldMappers: typing.Union[MetaOapg.properties.customOutboundFieldMappers, list, tuple, schemas.Unset] = schemas.unset,
        disabledFieldMappers: typing.Union['CreateAppConfigDisabledFieldMappers', schemas.Unset] = schemas.unset,
        enabledOutboundFieldMappers: typing.Union['CreateAppConfigEnabledOutboundFieldMappers', schemas.Unset] = schemas.unset,
        templateMatchers: typing.Union['CreateAppConfigTemplateMatchers', schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateAppConfig':
        return super().__new__(
            cls,
            *args,
            appId=appId,
            userId=userId,
            orgId=orgId,
            fieldMappers=fieldMappers,
            customFieldMappers=customFieldMappers,
            customOutboundFieldMappers=customOutboundFieldMappers,
            disabledFieldMappers=disabledFieldMappers,
            enabledOutboundFieldMappers=enabledOutboundFieldMappers,
            templateMatchers=templateMatchers,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.create_app_config_disabled_field_mappers import CreateAppConfigDisabledFieldMappers
from chart_hop_python_sdk.model.create_app_config_enabled_outbound_field_mappers import CreateAppConfigEnabledOutboundFieldMappers
from chart_hop_python_sdk.model.create_app_config_template_matchers import CreateAppConfigTemplateMatchers
from chart_hop_python_sdk.model.field_mapper import FieldMapper
from chart_hop_python_sdk.model.outbound_field_mapper import OutboundFieldMapper