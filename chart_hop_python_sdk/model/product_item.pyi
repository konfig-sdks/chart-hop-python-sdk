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


class ProductItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "productId",
            "stripePriceId",
        }
        
        class properties:
            productId = schemas.StrSchema
            stripePriceId = schemas.StrSchema
            __annotations__ = {
                "productId": productId,
                "stripePriceId": stripePriceId,
            }
    
    productId: MetaOapg.properties.productId
    stripePriceId: MetaOapg.properties.stripePriceId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productId"]) -> MetaOapg.properties.productId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripePriceId"]) -> MetaOapg.properties.stripePriceId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["productId", "stripePriceId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productId"]) -> MetaOapg.properties.productId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripePriceId"]) -> MetaOapg.properties.stripePriceId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["productId", "stripePriceId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        productId: typing.Union[MetaOapg.properties.productId, str, ],
        stripePriceId: typing.Union[MetaOapg.properties.stripePriceId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductItem':
        return super().__new__(
            cls,
            *args,
            productId=productId,
            stripePriceId=stripePriceId,
            _configuration=_configuration,
            **kwargs,
        )
