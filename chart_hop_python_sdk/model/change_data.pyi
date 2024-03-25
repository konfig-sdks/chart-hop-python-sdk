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


class ChangeData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "cost",
            "data",
            "change",
        }
        
        class properties:
        
            @staticmethod
            def change() -> typing.Type['Change']:
                return Change
        
            @staticmethod
            def data() -> typing.Type['ChangeDataData']:
                return ChangeDataData
            cost = schemas.NumberSchema
        
            @staticmethod
            def lockedFields() -> typing.Type['ChangeDataLockedFields']:
                return ChangeDataLockedFields
            __annotations__ = {
                "change": change,
                "data": data,
                "cost": cost,
                "lockedFields": lockedFields,
            }
    
    cost: MetaOapg.properties.cost
    data: 'ChangeDataData'
    change: 'Change'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["change"]) -> 'Change': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ChangeDataData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockedFields"]) -> 'ChangeDataLockedFields': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["change", "data", "cost", "lockedFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["change"]) -> 'Change': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ChangeDataData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockedFields"]) -> typing.Union['ChangeDataLockedFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["change", "data", "cost", "lockedFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cost: typing.Union[MetaOapg.properties.cost, decimal.Decimal, int, float, ],
        data: 'ChangeDataData',
        change: 'Change',
        lockedFields: typing.Union['ChangeDataLockedFields', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChangeData':
        return super().__new__(
            cls,
            *args,
            cost=cost,
            data=data,
            change=change,
            lockedFields=lockedFields,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.change import Change
from chart_hop_python_sdk.model.change_data_data import ChangeDataData
from chart_hop_python_sdk.model.change_data_locked_fields import ChangeDataLockedFields