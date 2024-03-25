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


class DueDate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "dueDay",
            "dueTime",
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXACT": "EXACT",
                        "RELATIVE": "RELATIVE",
                    }
                
                @schemas.classproperty
                def EXACT(cls):
                    return cls("EXACT")
                
                @schemas.classproperty
                def RELATIVE(cls):
                    return cls("RELATIVE")
            dueDay = schemas.StrSchema
            dueTime = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "dueDay": dueDay,
                "dueTime": dueTime,
            }
    
    dueDay: MetaOapg.properties.dueDay
    dueTime: MetaOapg.properties.dueTime
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dueDay"]) -> MetaOapg.properties.dueDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dueTime"]) -> MetaOapg.properties.dueTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "dueDay", "dueTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dueDay"]) -> MetaOapg.properties.dueDay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dueTime"]) -> MetaOapg.properties.dueTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "dueDay", "dueTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dueDay: typing.Union[MetaOapg.properties.dueDay, str, ],
        dueTime: typing.Union[MetaOapg.properties.dueTime, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DueDate':
        return super().__new__(
            cls,
            *args,
            dueDay=dueDay,
            dueTime=dueTime,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
