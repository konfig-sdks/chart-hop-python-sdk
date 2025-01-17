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


class SamlPerformSsoAssertionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            SAMLResponse = schemas.StrSchema
            RelayState = schemas.StrSchema
            __annotations__ = {
                "SAMLResponse": SAMLResponse,
                "RelayState": RelayState,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SAMLResponse"]) -> MetaOapg.properties.SAMLResponse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RelayState"]) -> MetaOapg.properties.RelayState: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["SAMLResponse", "RelayState", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SAMLResponse"]) -> typing.Union[MetaOapg.properties.SAMLResponse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RelayState"]) -> typing.Union[MetaOapg.properties.RelayState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SAMLResponse", "RelayState", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        SAMLResponse: typing.Union[MetaOapg.properties.SAMLResponse, str, schemas.Unset] = schemas.unset,
        RelayState: typing.Union[MetaOapg.properties.RelayState, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SamlPerformSsoAssertionRequest':
        return super().__new__(
            cls,
            *args,
            SAMLResponse=SAMLResponse,
            RelayState=RelayState,
            _configuration=_configuration,
            **kwargs,
        )
