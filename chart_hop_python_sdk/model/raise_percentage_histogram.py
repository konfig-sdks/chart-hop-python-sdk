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


class RaisePercentageHistogram(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "min",
            "max",
            "buckets",
            "increment",
        }
        
        class properties:
            min = schemas.NumberSchema
            max = schemas.NumberSchema
            increment = schemas.NumberSchema
            
            
            class buckets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Bucket']:
                        return Bucket
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Bucket'], typing.List['Bucket']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'buckets':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Bucket':
                    return super().__getitem__(i)
            __annotations__ = {
                "min": min,
                "max": max,
                "increment": increment,
                "buckets": buckets,
            }
    
    min: MetaOapg.properties.min
    max: MetaOapg.properties.max
    buckets: MetaOapg.properties.buckets
    increment: MetaOapg.properties.increment
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["increment"]) -> MetaOapg.properties.increment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buckets"]) -> MetaOapg.properties.buckets: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["min", "max", "increment", "buckets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["increment"]) -> MetaOapg.properties.increment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buckets"]) -> MetaOapg.properties.buckets: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["min", "max", "increment", "buckets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, float, ],
        max: typing.Union[MetaOapg.properties.max, decimal.Decimal, int, float, ],
        buckets: typing.Union[MetaOapg.properties.buckets, list, tuple, ],
        increment: typing.Union[MetaOapg.properties.increment, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RaisePercentageHistogram':
        return super().__new__(
            cls,
            *args,
            min=min,
            max=max,
            buckets=buckets,
            increment=increment,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.bucket import Bucket