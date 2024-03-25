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


class ApprovalGroupApprover(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "jobId",
            "status",
        }
        
        class properties:
            jobId = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PENDING": "PENDING",
                        "APPROVED": "APPROVED",
                        "REJECTED": "REJECTED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("APPROVED")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("REJECTED")
            commentId = schemas.StrSchema
            reassignCommentId = schemas.StrSchema
            isFallback = schemas.BoolSchema
            fallbackFor = schemas.StrSchema
            updateAt = schemas.Int64Schema
            __annotations__ = {
                "jobId": jobId,
                "status": status,
                "commentId": commentId,
                "reassignCommentId": reassignCommentId,
                "isFallback": isFallback,
                "fallbackFor": fallbackFor,
                "updateAt": updateAt,
            }
    
    jobId: MetaOapg.properties.jobId
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commentId"]) -> MetaOapg.properties.commentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reassignCommentId"]) -> MetaOapg.properties.reassignCommentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFallback"]) -> MetaOapg.properties.isFallback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fallbackFor"]) -> MetaOapg.properties.fallbackFor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobId", "status", "commentId", "reassignCommentId", "isFallback", "fallbackFor", "updateAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commentId"]) -> typing.Union[MetaOapg.properties.commentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reassignCommentId"]) -> typing.Union[MetaOapg.properties.reassignCommentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFallback"]) -> typing.Union[MetaOapg.properties.isFallback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fallbackFor"]) -> typing.Union[MetaOapg.properties.fallbackFor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> typing.Union[MetaOapg.properties.updateAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobId", "status", "commentId", "reassignCommentId", "isFallback", "fallbackFor", "updateAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jobId: typing.Union[MetaOapg.properties.jobId, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        commentId: typing.Union[MetaOapg.properties.commentId, str, schemas.Unset] = schemas.unset,
        reassignCommentId: typing.Union[MetaOapg.properties.reassignCommentId, str, schemas.Unset] = schemas.unset,
        isFallback: typing.Union[MetaOapg.properties.isFallback, bool, schemas.Unset] = schemas.unset,
        fallbackFor: typing.Union[MetaOapg.properties.fallbackFor, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApprovalGroupApprover':
        return super().__new__(
            cls,
            *args,
            jobId=jobId,
            status=status,
            commentId=commentId,
            reassignCommentId=reassignCommentId,
            isFallback=isFallback,
            fallbackFor=fallbackFor,
            updateAt=updateAt,
            _configuration=_configuration,
            **kwargs,
        )