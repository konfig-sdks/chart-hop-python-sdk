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


class GrantAlias(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "grantType",
            "enabled",
        }
        
        class properties:
            
            
            class grantType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ISO(cls):
                    return cls("ISO")
                
                @schemas.classproperty
                def NSO(cls):
                    return cls("NSO")
                
                @schemas.classproperty
                def RSU(cls):
                    return cls("RSU")
                
                @schemas.classproperty
                def SAR(cls):
                    return cls("SAR")
                
                @schemas.classproperty
                def PERFORMANCE_SHARES(cls):
                    return cls("PERFORMANCE_SHARES")
                
                @schemas.classproperty
                def PHANTOM_STOCK(cls):
                    return cls("PHANTOM_STOCK")
                
                @schemas.classproperty
                def RSA(cls):
                    return cls("RSA")
            enabled = schemas.BoolSchema
            alias = schemas.StrSchema
            __annotations__ = {
                "grantType": grantType,
                "enabled": enabled,
                "alias": alias,
            }
    
    grantType: MetaOapg.properties.grantType
    enabled: MetaOapg.properties.enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantType"]) -> MetaOapg.properties.grantType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alias"]) -> MetaOapg.properties.alias: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["grantType", "enabled", "alias", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantType"]) -> MetaOapg.properties.grantType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alias"]) -> typing.Union[MetaOapg.properties.alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["grantType", "enabled", "alias", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grantType: typing.Union[MetaOapg.properties.grantType, str, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        alias: typing.Union[MetaOapg.properties.alias, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GrantAlias':
        return super().__new__(
            cls,
            *args,
            grantType=grantType,
            enabled=enabled,
            alias=alias,
            _configuration=_configuration,
            **kwargs,
        )
