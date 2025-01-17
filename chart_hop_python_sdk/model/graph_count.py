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


class GraphCount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sibling",
            "underUnfilled",
            "siblingUnfilled",
            "under",
        }
        
        class properties:
            under = schemas.Int32Schema
            sibling = schemas.Int32Schema
            underUnfilled = schemas.Int32Schema
            siblingUnfilled = schemas.Int32Schema
            __annotations__ = {
                "under": under,
                "sibling": sibling,
                "underUnfilled": underUnfilled,
                "siblingUnfilled": siblingUnfilled,
            }
    
    sibling: MetaOapg.properties.sibling
    underUnfilled: MetaOapg.properties.underUnfilled
    siblingUnfilled: MetaOapg.properties.siblingUnfilled
    under: MetaOapg.properties.under
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["under"]) -> MetaOapg.properties.under: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sibling"]) -> MetaOapg.properties.sibling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["underUnfilled"]) -> MetaOapg.properties.underUnfilled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siblingUnfilled"]) -> MetaOapg.properties.siblingUnfilled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["under", "sibling", "underUnfilled", "siblingUnfilled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["under"]) -> MetaOapg.properties.under: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sibling"]) -> MetaOapg.properties.sibling: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["underUnfilled"]) -> MetaOapg.properties.underUnfilled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siblingUnfilled"]) -> MetaOapg.properties.siblingUnfilled: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["under", "sibling", "underUnfilled", "siblingUnfilled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sibling: typing.Union[MetaOapg.properties.sibling, decimal.Decimal, int, ],
        underUnfilled: typing.Union[MetaOapg.properties.underUnfilled, decimal.Decimal, int, ],
        siblingUnfilled: typing.Union[MetaOapg.properties.siblingUnfilled, decimal.Decimal, int, ],
        under: typing.Union[MetaOapg.properties.under, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GraphCount':
        return super().__new__(
            cls,
            *args,
            sibling=sibling,
            underUnfilled=underUnfilled,
            siblingUnfilled=siblingUnfilled,
            under=under,
            _configuration=_configuration,
            **kwargs,
        )
