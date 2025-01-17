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


class Task(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entityId",
            "id",
            "type",
            "userId",
            "orgId",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            userId = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "FORM_SUBMIT": "FORM_SUBMIT",
                        "CHANGE_APPROVE": "CHANGE_APPROVE",
                        "TIMEOFF_APPROVE": "TIMEOFF_APPROVE",
                        "SCENARIO_CHANGES_APPROVE": "SCENARIO_CHANGES_APPROVE",
                        "SCENARIO_CHANGES_CREATE": "SCENARIO_CHANGES_CREATE",
                        "ORG_IMPORT": "ORG_IMPORT",
                        "COMP_REVIEW_APPROVAL_SUBMIT": "COMP_REVIEW_APPROVAL_SUBMIT",
                        "SCENARIO_APPROVAL_SUBMIT": "SCENARIO_APPROVAL_SUBMIT",
                        "APPROVAL_CHAIN_UPDATE_FALLBACK_APPROVER": "APPROVAL_CHAIN_UPDATE_FALLBACK_APPROVER",
                        "ACTION": "ACTION",
                    }
                
                @schemas.classproperty
                def FORM_SUBMIT(cls):
                    return cls("FORM_SUBMIT")
                
                @schemas.classproperty
                def CHANGE_APPROVE(cls):
                    return cls("CHANGE_APPROVE")
                
                @schemas.classproperty
                def TIMEOFF_APPROVE(cls):
                    return cls("TIMEOFF_APPROVE")
                
                @schemas.classproperty
                def SCENARIO_CHANGES_APPROVE(cls):
                    return cls("SCENARIO_CHANGES_APPROVE")
                
                @schemas.classproperty
                def SCENARIO_CHANGES_CREATE(cls):
                    return cls("SCENARIO_CHANGES_CREATE")
                
                @schemas.classproperty
                def ORG_IMPORT(cls):
                    return cls("ORG_IMPORT")
                
                @schemas.classproperty
                def COMP_REVIEW_APPROVAL_SUBMIT(cls):
                    return cls("COMP_REVIEW_APPROVAL_SUBMIT")
                
                @schemas.classproperty
                def SCENARIO_APPROVAL_SUBMIT(cls):
                    return cls("SCENARIO_APPROVAL_SUBMIT")
                
                @schemas.classproperty
                def APPROVAL_CHAIN_UPDATE_FALLBACK_APPROVER(cls):
                    return cls("APPROVAL_CHAIN_UPDATE_FALLBACK_APPROVER")
                
                @schemas.classproperty
                def ACTION(cls):
                    return cls("ACTION")
            entityId = schemas.StrSchema
            
            
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
            assessmentId = schemas.StrSchema
            parentEntityId = schemas.StrSchema
            targetId = schemas.StrSchema
            doneAt = schemas.StrSchema
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
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
            path = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
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
                "id": id,
                "orgId": orgId,
                "userId": userId,
                "type": type,
                "entityId": entityId,
                "status": status,
                "assessmentId": assessmentId,
                "parentEntityId": parentEntityId,
                "targetId": targetId,
                "doneAt": doneAt,
                "createId": createId,
                "createAt": createAt,
                "message": message,
                "shareAccess": shareAccess,
                "path": path,
                "updateId": updateId,
                "updateAt": updateAt,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
                "taskConfigId": taskConfigId,
                "slug": slug,
                "dueAt": dueAt,
                "pastDueAction": pastDueAction,
                "isSkippable": isSkippable,
            }
    
    entityId: MetaOapg.properties.entityId
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    userId: MetaOapg.properties.userId
    orgId: MetaOapg.properties.orgId
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assessmentId"]) -> MetaOapg.properties.assessmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentEntityId"]) -> MetaOapg.properties.parentEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetId"]) -> MetaOapg.properties.targetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doneAt"]) -> MetaOapg.properties.doneAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteId"]) -> MetaOapg.properties.deleteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteAt"]) -> MetaOapg.properties.deleteAt: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "userId", "type", "entityId", "status", "assessmentId", "parentEntityId", "targetId", "doneAt", "createId", "createAt", "message", "shareAccess", "path", "updateId", "updateAt", "deleteId", "deleteAt", "taskConfigId", "slug", "dueAt", "pastDueAction", "isSkippable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assessmentId"]) -> typing.Union[MetaOapg.properties.assessmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentEntityId"]) -> typing.Union[MetaOapg.properties.parentEntityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetId"]) -> typing.Union[MetaOapg.properties.targetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doneAt"]) -> typing.Union[MetaOapg.properties.doneAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createId"]) -> typing.Union[MetaOapg.properties.createId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> typing.Union[MetaOapg.properties.createAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> typing.Union[MetaOapg.properties.updateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> typing.Union[MetaOapg.properties.updateAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteId"]) -> typing.Union[MetaOapg.properties.deleteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteAt"]) -> typing.Union[MetaOapg.properties.deleteAt, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "userId", "type", "entityId", "status", "assessmentId", "parentEntityId", "targetId", "doneAt", "createId", "createAt", "message", "shareAccess", "path", "updateId", "updateAt", "deleteId", "deleteAt", "taskConfigId", "slug", "dueAt", "pastDueAction", "isSkippable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entityId: typing.Union[MetaOapg.properties.entityId, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        assessmentId: typing.Union[MetaOapg.properties.assessmentId, str, schemas.Unset] = schemas.unset,
        parentEntityId: typing.Union[MetaOapg.properties.parentEntityId, str, schemas.Unset] = schemas.unset,
        targetId: typing.Union[MetaOapg.properties.targetId, str, schemas.Unset] = schemas.unset,
        doneAt: typing.Union[MetaOapg.properties.doneAt, str, schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        taskConfigId: typing.Union[MetaOapg.properties.taskConfigId, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        dueAt: typing.Union[MetaOapg.properties.dueAt, str, schemas.Unset] = schemas.unset,
        pastDueAction: typing.Union[MetaOapg.properties.pastDueAction, str, schemas.Unset] = schemas.unset,
        isSkippable: typing.Union[MetaOapg.properties.isSkippable, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Task':
        return super().__new__(
            cls,
            *args,
            entityId=entityId,
            id=id,
            type=type,
            userId=userId,
            orgId=orgId,
            status=status,
            assessmentId=assessmentId,
            parentEntityId=parentEntityId,
            targetId=targetId,
            doneAt=doneAt,
            createId=createId,
            createAt=createAt,
            message=message,
            shareAccess=shareAccess,
            path=path,
            updateId=updateId,
            updateAt=updateAt,
            deleteId=deleteId,
            deleteAt=deleteAt,
            taskConfigId=taskConfigId,
            slug=slug,
            dueAt=dueAt,
            pastDueAction=pastDueAction,
            isSkippable=isSkippable,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.share_access import ShareAccess
