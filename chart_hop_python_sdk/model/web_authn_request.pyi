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


class WebAuthnRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "requestId",
            "credentialResponse",
        }
        
        class properties:
            requestId = schemas.StrSchema
            credentialResponse = schemas.StrSchema
            __annotations__ = {
                "requestId": requestId,
                "credentialResponse": credentialResponse,
            }
    
    requestId: MetaOapg.properties.requestId
    credentialResponse: MetaOapg.properties.credentialResponse
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credentialResponse"]) -> MetaOapg.properties.credentialResponse: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["requestId", "credentialResponse", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credentialResponse"]) -> MetaOapg.properties.credentialResponse: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["requestId", "credentialResponse", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        requestId: typing.Union[MetaOapg.properties.requestId, str, ],
        credentialResponse: typing.Union[MetaOapg.properties.credentialResponse, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebAuthnRequest':
        return super().__new__(
            cls,
            *args,
            requestId=requestId,
            credentialResponse=credentialResponse,
            _configuration=_configuration,
            **kwargs,
        )