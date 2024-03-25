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


class UpdateTask(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PENDING": "PENDING",
                        "DONE": "DONE",
                        "EXPIRED": "EXPIRED",
                        "SKIPPED": "SKIPPED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("DONE")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("EXPIRED")
                
                @schemas.classproperty
                def SKIPPED(cls):
                    return cls("SKIPPED")
            message = schemas.StrSchema
            
            
            class shareAccess(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShareAccess']:
                        return ShareAccess
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ShareAccess'], typing.List['ShareAccess']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shareAccess':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShareAccess':
                    return super().__getitem__(i)
            taskConfigId = schemas.StrSchema
            slug = schemas.StrSchema
            dueAt = schemas.StrSchema
            
            
            class pastDueAction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NONE": "NONE",
                        "SET_EXPIRED": "SET_EXPIRED",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def SET_EXPIRED(cls):
                    return cls("SET_EXPIRED")
            isSkippable = schemas.BoolSchema
            __annotations__ = {
                "status": status,
                "message": message,
                "shareAccess": shareAccess,
                "taskConfigId": taskConfigId,
                "slug": slug,
                "dueAt": dueAt,
                "pastDueAction": pastDueAction,
                "isSkippable": isSkippable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskConfigId"]) -> MetaOapg.properties.taskConfigId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dueAt"]) -> MetaOapg.properties.dueAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pastDueAction"]) -> MetaOapg.properties.pastDueAction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSkippable"]) -> MetaOapg.properties.isSkippable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "message", "shareAccess", "taskConfigId", "slug", "dueAt", "pastDueAction", "isSkippable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskConfigId"]) -> typing.Union[MetaOapg.properties.taskConfigId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dueAt"]) -> typing.Union[MetaOapg.properties.dueAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pastDueAction"]) -> typing.Union[MetaOapg.properties.pastDueAction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSkippable"]) -> typing.Union[MetaOapg.properties.isSkippable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "message", "shareAccess", "taskConfigId", "slug", "dueAt", "pastDueAction", "isSkippable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        taskConfigId: typing.Union[MetaOapg.properties.taskConfigId, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        dueAt: typing.Union[MetaOapg.properties.dueAt, str, schemas.Unset] = schemas.unset,
        pastDueAction: typing.Union[MetaOapg.properties.pastDueAction, str, schemas.Unset] = schemas.unset,
        isSkippable: typing.Union[MetaOapg.properties.isSkippable, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateTask':
        return super().__new__(
            cls,
            *args,
            status=status,
            message=message,
            shareAccess=shareAccess,
            taskConfigId=taskConfigId,
            slug=slug,
            dueAt=dueAt,
            pastDueAction=pastDueAction,
            isSkippable=isSkippable,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.share_access import ShareAccess