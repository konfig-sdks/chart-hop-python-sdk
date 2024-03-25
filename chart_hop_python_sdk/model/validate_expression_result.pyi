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


class ValidateExpressionResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "isValid",
            "expr",
            "message",
        }
        
        class properties:
            expr = schemas.StrSchema
            isValid = schemas.BoolSchema
            message = schemas.StrSchema
            __annotations__ = {
                "expr": expr,
                "isValid": isValid,
                "message": message,
            }
    
    isValid: MetaOapg.properties.isValid
    expr: MetaOapg.properties.expr
    message: MetaOapg.properties.message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expr"]) -> MetaOapg.properties.expr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isValid"]) -> MetaOapg.properties.isValid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expr", "isValid", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expr"]) -> MetaOapg.properties.expr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isValid"]) -> MetaOapg.properties.isValid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expr", "isValid", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isValid: typing.Union[MetaOapg.properties.isValid, bool, ],
        expr: typing.Union[MetaOapg.properties.expr, str, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ValidateExpressionResult':
        return super().__new__(
            cls,
            *args,
            isValid=isValid,
            expr=expr,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )