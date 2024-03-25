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


class CreateEmailTemplate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "category",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class category(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ADMINISTRATIVE": "ADMINISTRATIVE",
                        "BILLING": "BILLING",
                        "DATA_IMPORT_AND_SYNC_STATUS": "DATA_IMPORT_AND_SYNC_STATUS",
                        "TRIAL_REMINDERS": "TRIAL_REMINDERS",
                    }
                
                @schemas.classproperty
                def ADMINISTRATIVE(cls):
                    return cls("ADMINISTRATIVE")
                
                @schemas.classproperty
                def BILLING(cls):
                    return cls("BILLING")
                
                @schemas.classproperty
                def DATA_IMPORT_AND_SYNC_STATUS(cls):
                    return cls("DATA_IMPORT_AND_SYNC_STATUS")
                
                @schemas.classproperty
                def TRIAL_REMINDERS(cls):
                    return cls("TRIAL_REMINDERS")
            __annotations__ = {
                "name": name,
                "category": category,
            }
    
    name: MetaOapg.properties.name
    category: MetaOapg.properties.category
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "category", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "category", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateEmailTemplate':
        return super().__new__(
            cls,
            *args,
            name=name,
            category=category,
            _configuration=_configuration,
            **kwargs,
        )