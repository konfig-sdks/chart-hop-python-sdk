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


class ActionStep(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FORM(cls):
                    return cls("FORM")
                
                @schemas.classproperty
                def MESSAGE(cls):
                    return cls("MESSAGE")
                
                @schemas.classproperty
                def HTTP(cls):
                    return cls("HTTP")
                
                @schemas.classproperty
                def TASK(cls):
                    return cls("TASK")
            stepId = schemas.StrSchema
            formId = schemas.StrSchema
            target = schemas.StrSchema
            assignee = schemas.StrSchema
            message = schemas.StrSchema
            emailSubject = schemas.StrSchema
            sensitive = schemas.BoolSchema
            httpUrl = schemas.StrSchema
            httpMethod = schemas.StrSchema
        
            @staticmethod
            def httpHeaders() -> typing.Type['ActionStepHttpHeaders']:
                return ActionStepHttpHeaders
            httpContent = schemas.DictSchema
            __annotations__ = {
                "type": type,
                "stepId": stepId,
                "formId": formId,
                "target": target,
                "assignee": assignee,
                "message": message,
                "emailSubject": emailSubject,
                "sensitive": sensitive,
                "httpUrl": httpUrl,
                "httpMethod": httpMethod,
                "httpHeaders": httpHeaders,
                "httpContent": httpContent,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepId"]) -> MetaOapg.properties.stepId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["formId"]) -> MetaOapg.properties.formId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailSubject"]) -> MetaOapg.properties.emailSubject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpUrl"]) -> MetaOapg.properties.httpUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpMethod"]) -> MetaOapg.properties.httpMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpHeaders"]) -> 'ActionStepHttpHeaders': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpContent"]) -> MetaOapg.properties.httpContent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "stepId", "formId", "target", "assignee", "message", "emailSubject", "sensitive", "httpUrl", "httpMethod", "httpHeaders", "httpContent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepId"]) -> typing.Union[MetaOapg.properties.stepId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["formId"]) -> typing.Union[MetaOapg.properties.formId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> typing.Union[MetaOapg.properties.target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> typing.Union[MetaOapg.properties.assignee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailSubject"]) -> typing.Union[MetaOapg.properties.emailSubject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitive"]) -> typing.Union[MetaOapg.properties.sensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpUrl"]) -> typing.Union[MetaOapg.properties.httpUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpMethod"]) -> typing.Union[MetaOapg.properties.httpMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpHeaders"]) -> typing.Union['ActionStepHttpHeaders', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpContent"]) -> typing.Union[MetaOapg.properties.httpContent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "stepId", "formId", "target", "assignee", "message", "emailSubject", "sensitive", "httpUrl", "httpMethod", "httpHeaders", "httpContent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        stepId: typing.Union[MetaOapg.properties.stepId, str, schemas.Unset] = schemas.unset,
        formId: typing.Union[MetaOapg.properties.formId, str, schemas.Unset] = schemas.unset,
        target: typing.Union[MetaOapg.properties.target, str, schemas.Unset] = schemas.unset,
        assignee: typing.Union[MetaOapg.properties.assignee, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        emailSubject: typing.Union[MetaOapg.properties.emailSubject, str, schemas.Unset] = schemas.unset,
        sensitive: typing.Union[MetaOapg.properties.sensitive, bool, schemas.Unset] = schemas.unset,
        httpUrl: typing.Union[MetaOapg.properties.httpUrl, str, schemas.Unset] = schemas.unset,
        httpMethod: typing.Union[MetaOapg.properties.httpMethod, str, schemas.Unset] = schemas.unset,
        httpHeaders: typing.Union['ActionStepHttpHeaders', schemas.Unset] = schemas.unset,
        httpContent: typing.Union[MetaOapg.properties.httpContent, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ActionStep':
        return super().__new__(
            cls,
            *args,
            type=type,
            stepId=stepId,
            formId=formId,
            target=target,
            assignee=assignee,
            message=message,
            emailSubject=emailSubject,
            sensitive=sensitive,
            httpUrl=httpUrl,
            httpMethod=httpMethod,
            httpHeaders=httpHeaders,
            httpContent=httpContent,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.action_step_http_headers import ActionStepHttpHeaders
