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


class Name(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "last",
        }
        
        class properties:
            last = schemas.StrSchema
            first = schemas.StrSchema
            middle = schemas.StrSchema
            pref = schemas.StrSchema
            prefLast = schemas.StrSchema
            __annotations__ = {
                "last": last,
                "first": first,
                "middle": middle,
                "pref": pref,
                "prefLast": prefLast,
            }
    
    last: MetaOapg.properties.last
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middle"]) -> MetaOapg.properties.middle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pref"]) -> MetaOapg.properties.pref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefLast"]) -> MetaOapg.properties.prefLast: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["last", "first", "middle", "pref", "prefLast", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union[MetaOapg.properties.first, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middle"]) -> typing.Union[MetaOapg.properties.middle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pref"]) -> typing.Union[MetaOapg.properties.pref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefLast"]) -> typing.Union[MetaOapg.properties.prefLast, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["last", "first", "middle", "pref", "prefLast", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        last: typing.Union[MetaOapg.properties.last, str, ],
        first: typing.Union[MetaOapg.properties.first, str, schemas.Unset] = schemas.unset,
        middle: typing.Union[MetaOapg.properties.middle, str, schemas.Unset] = schemas.unset,
        pref: typing.Union[MetaOapg.properties.pref, str, schemas.Unset] = schemas.unset,
        prefLast: typing.Union[MetaOapg.properties.prefLast, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Name':
        return super().__new__(
            cls,
            *args,
            last=last,
            first=first,
            middle=middle,
            pref=pref,
            prefLast=prefLast,
            _configuration=_configuration,
            **kwargs,
        )
