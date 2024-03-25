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


class NotifyRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            emailSubject = schemas.StrSchema
            emailContentHtml = schemas.StrSchema
            emailMarkdown = schemas.StrSchema
            chatMarkdown = schemas.StrSchema
            notifyType = schemas.StrSchema
            __annotations__ = {
                "emailSubject": emailSubject,
                "emailContentHtml": emailContentHtml,
                "emailMarkdown": emailMarkdown,
                "chatMarkdown": chatMarkdown,
                "notifyType": notifyType,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailSubject"]) -> MetaOapg.properties.emailSubject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailContentHtml"]) -> MetaOapg.properties.emailContentHtml: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailMarkdown"]) -> MetaOapg.properties.emailMarkdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chatMarkdown"]) -> MetaOapg.properties.chatMarkdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifyType"]) -> MetaOapg.properties.notifyType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["emailSubject", "emailContentHtml", "emailMarkdown", "chatMarkdown", "notifyType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailSubject"]) -> typing.Union[MetaOapg.properties.emailSubject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailContentHtml"]) -> typing.Union[MetaOapg.properties.emailContentHtml, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailMarkdown"]) -> typing.Union[MetaOapg.properties.emailMarkdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chatMarkdown"]) -> typing.Union[MetaOapg.properties.chatMarkdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifyType"]) -> typing.Union[MetaOapg.properties.notifyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["emailSubject", "emailContentHtml", "emailMarkdown", "chatMarkdown", "notifyType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        emailSubject: typing.Union[MetaOapg.properties.emailSubject, str, schemas.Unset] = schemas.unset,
        emailContentHtml: typing.Union[MetaOapg.properties.emailContentHtml, str, schemas.Unset] = schemas.unset,
        emailMarkdown: typing.Union[MetaOapg.properties.emailMarkdown, str, schemas.Unset] = schemas.unset,
        chatMarkdown: typing.Union[MetaOapg.properties.chatMarkdown, str, schemas.Unset] = schemas.unset,
        notifyType: typing.Union[MetaOapg.properties.notifyType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NotifyRequest':
        return super().__new__(
            cls,
            *args,
            emailSubject=emailSubject,
            emailContentHtml=emailContentHtml,
            emailMarkdown=emailMarkdown,
            chatMarkdown=chatMarkdown,
            notifyType=notifyType,
            _configuration=_configuration,
            **kwargs,
        )
