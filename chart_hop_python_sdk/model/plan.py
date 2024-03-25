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


class Plan(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "tiers",
            "stripeProductId",
            "intervalCount",
            "name",
            "interval",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class interval(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DAY": "DAY",
                        "WEEK": "WEEK",
                        "MONTH": "MONTH",
                        "YEAR": "YEAR",
                    }
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("DAY")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("WEEK")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("MONTH")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("YEAR")
            intervalCount = schemas.Int32Schema
            
            
            class tiers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PlanTier']:
                        return PlanTier
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PlanTier'], typing.List['PlanTier']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tiers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PlanTier':
                    return super().__getitem__(i)
            stripeProductId = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "interval": interval,
                "intervalCount": intervalCount,
                "tiers": tiers,
                "stripeProductId": stripeProductId,
            }
    
    tiers: MetaOapg.properties.tiers
    stripeProductId: MetaOapg.properties.stripeProductId
    intervalCount: MetaOapg.properties.intervalCount
    name: MetaOapg.properties.name
    interval: MetaOapg.properties.interval
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intervalCount"]) -> MetaOapg.properties.intervalCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tiers"]) -> MetaOapg.properties.tiers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripeProductId"]) -> MetaOapg.properties.stripeProductId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "interval", "intervalCount", "tiers", "stripeProductId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intervalCount"]) -> MetaOapg.properties.intervalCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tiers"]) -> MetaOapg.properties.tiers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripeProductId"]) -> MetaOapg.properties.stripeProductId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "interval", "intervalCount", "tiers", "stripeProductId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tiers: typing.Union[MetaOapg.properties.tiers, list, tuple, ],
        stripeProductId: typing.Union[MetaOapg.properties.stripeProductId, str, ],
        intervalCount: typing.Union[MetaOapg.properties.intervalCount, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        interval: typing.Union[MetaOapg.properties.interval, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Plan':
        return super().__new__(
            cls,
            *args,
            tiers=tiers,
            stripeProductId=stripeProductId,
            intervalCount=intervalCount,
            name=name,
            interval=interval,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.plan_tier import PlanTier