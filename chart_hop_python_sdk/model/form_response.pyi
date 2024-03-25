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


class FormResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            externalId = schemas.StrSchema
            formId = schemas.StrSchema
            formVersionId = schemas.StrSchema
            submitPersonId = schemas.StrSchema
            submitUserId = schemas.StrSchema
            changeId = schemas.StrSchema
            assessmentId = schemas.StrSchema
            
            
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
            
            
            class authorSensitive(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ANONYMOUS(cls):
                    return cls("ANONYMOUS")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
                
                @schemas.classproperty
                def HIGH(cls):
                    return cls("HIGH")
                
                @schemas.classproperty
                def MANAGER(cls):
                    return cls("MANAGER")
            targetEntityId = schemas.StrSchema
            
            
            class targetEntityType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def PERSON(cls):
                    return cls("PERSON")
            
            
            class answers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FormResponseAnswer']:
                        return FormResponseAnswer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FormResponseAnswer'], typing.List['FormResponseAnswer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'answers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FormResponseAnswer':
                    return super().__getitem__(i)
            submitAt = schemas.Int64Schema
            approvalAt = schemas.Int64Schema
            approvalId = schemas.StrSchema
            approvalNote = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def PROPOSED(cls):
                    return cls("PROPOSED")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("REJECTED")
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "orgId": orgId,
                "externalId": externalId,
                "formId": formId,
                "formVersionId": formVersionId,
                "submitPersonId": submitPersonId,
                "submitUserId": submitUserId,
                "changeId": changeId,
                "assessmentId": assessmentId,
                "shareAccess": shareAccess,
                "authorSensitive": authorSensitive,
                "targetEntityId": targetEntityId,
                "targetEntityType": targetEntityType,
                "answers": answers,
                "submitAt": submitAt,
                "approvalAt": approvalAt,
                "approvalId": approvalId,
                "approvalNote": approvalNote,
                "status": status,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
            }
    
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalId"]) -> MetaOapg.properties.externalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["formId"]) -> MetaOapg.properties.formId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["formVersionId"]) -> MetaOapg.properties.formVersionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitPersonId"]) -> MetaOapg.properties.submitPersonId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitUserId"]) -> MetaOapg.properties.submitUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changeId"]) -> MetaOapg.properties.changeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assessmentId"]) -> MetaOapg.properties.assessmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorSensitive"]) -> MetaOapg.properties.authorSensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetEntityId"]) -> MetaOapg.properties.targetEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetEntityType"]) -> MetaOapg.properties.targetEntityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answers"]) -> MetaOapg.properties.answers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitAt"]) -> MetaOapg.properties.submitAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalAt"]) -> MetaOapg.properties.approvalAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalId"]) -> MetaOapg.properties.approvalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalNote"]) -> MetaOapg.properties.approvalNote: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteId"]) -> MetaOapg.properties.deleteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteAt"]) -> MetaOapg.properties.deleteAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "externalId", "formId", "formVersionId", "submitPersonId", "submitUserId", "changeId", "assessmentId", "shareAccess", "authorSensitive", "targetEntityId", "targetEntityType", "answers", "submitAt", "approvalAt", "approvalId", "approvalNote", "status", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalId"]) -> typing.Union[MetaOapg.properties.externalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["formId"]) -> typing.Union[MetaOapg.properties.formId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["formVersionId"]) -> typing.Union[MetaOapg.properties.formVersionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitPersonId"]) -> typing.Union[MetaOapg.properties.submitPersonId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitUserId"]) -> typing.Union[MetaOapg.properties.submitUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changeId"]) -> typing.Union[MetaOapg.properties.changeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assessmentId"]) -> typing.Union[MetaOapg.properties.assessmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorSensitive"]) -> typing.Union[MetaOapg.properties.authorSensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetEntityId"]) -> typing.Union[MetaOapg.properties.targetEntityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetEntityType"]) -> typing.Union[MetaOapg.properties.targetEntityType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answers"]) -> typing.Union[MetaOapg.properties.answers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitAt"]) -> typing.Union[MetaOapg.properties.submitAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalAt"]) -> typing.Union[MetaOapg.properties.approvalAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalId"]) -> typing.Union[MetaOapg.properties.approvalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalNote"]) -> typing.Union[MetaOapg.properties.approvalNote, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createId"]) -> typing.Union[MetaOapg.properties.createId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> typing.Union[MetaOapg.properties.createAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> typing.Union[MetaOapg.properties.updateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> typing.Union[MetaOapg.properties.updateAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteId"]) -> typing.Union[MetaOapg.properties.deleteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteAt"]) -> typing.Union[MetaOapg.properties.deleteAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "externalId", "formId", "formVersionId", "submitPersonId", "submitUserId", "changeId", "assessmentId", "shareAccess", "authorSensitive", "targetEntityId", "targetEntityType", "answers", "submitAt", "approvalAt", "approvalId", "approvalNote", "status", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        externalId: typing.Union[MetaOapg.properties.externalId, str, schemas.Unset] = schemas.unset,
        formId: typing.Union[MetaOapg.properties.formId, str, schemas.Unset] = schemas.unset,
        formVersionId: typing.Union[MetaOapg.properties.formVersionId, str, schemas.Unset] = schemas.unset,
        submitPersonId: typing.Union[MetaOapg.properties.submitPersonId, str, schemas.Unset] = schemas.unset,
        submitUserId: typing.Union[MetaOapg.properties.submitUserId, str, schemas.Unset] = schemas.unset,
        changeId: typing.Union[MetaOapg.properties.changeId, str, schemas.Unset] = schemas.unset,
        assessmentId: typing.Union[MetaOapg.properties.assessmentId, str, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        authorSensitive: typing.Union[MetaOapg.properties.authorSensitive, str, schemas.Unset] = schemas.unset,
        targetEntityId: typing.Union[MetaOapg.properties.targetEntityId, str, schemas.Unset] = schemas.unset,
        targetEntityType: typing.Union[MetaOapg.properties.targetEntityType, str, schemas.Unset] = schemas.unset,
        answers: typing.Union[MetaOapg.properties.answers, list, tuple, schemas.Unset] = schemas.unset,
        submitAt: typing.Union[MetaOapg.properties.submitAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        approvalAt: typing.Union[MetaOapg.properties.approvalAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        approvalId: typing.Union[MetaOapg.properties.approvalId, str, schemas.Unset] = schemas.unset,
        approvalNote: typing.Union[MetaOapg.properties.approvalNote, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            orgId=orgId,
            externalId=externalId,
            formId=formId,
            formVersionId=formVersionId,
            submitPersonId=submitPersonId,
            submitUserId=submitUserId,
            changeId=changeId,
            assessmentId=assessmentId,
            shareAccess=shareAccess,
            authorSensitive=authorSensitive,
            targetEntityId=targetEntityId,
            targetEntityType=targetEntityType,
            answers=answers,
            submitAt=submitAt,
            approvalAt=approvalAt,
            approvalId=approvalId,
            approvalNote=approvalNote,
            status=status,
            createId=createId,
            createAt=createAt,
            updateId=updateId,
            updateAt=updateAt,
            deleteId=deleteId,
            deleteAt=deleteAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.form_response_answer import FormResponseAnswer
from chart_hop_python_sdk.model.share_access import ShareAccess
