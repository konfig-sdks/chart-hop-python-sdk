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


class PartialForm(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            label = schemas.StrSchema
            
            
            class fields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FormField']:
                        return FormField
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FormField'], typing.List['FormField']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fields':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FormField':
                    return super().__getitem__(i)
            
            
            class blocks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FormBlock']:
                        return FormBlock
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FormBlock'], typing.List['FormBlock']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'blocks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FormBlock':
                    return super().__getitem__(i)
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def ARCHIVED(cls):
                    return cls("ARCHIVED")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BUILT_IN(cls):
                    return cls("BUILT_IN")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("CUSTOM")
            
            
            class sensitive(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GLOBAL(cls):
                    return cls("GLOBAL")
                
                @schemas.classproperty
                def ORG(cls):
                    return cls("ORG")
                
                @schemas.classproperty
                def ORG_OTHER(cls):
                    return cls("ORG_OTHER")
                
                @schemas.classproperty
                def PERSONAL_DEMOG(cls):
                    return cls("PERSONAL_DEMOG")
                
                @schemas.classproperty
                def PERSONAL_BIRTH(cls):
                    return cls("PERSONAL_BIRTH")
                
                @schemas.classproperty
                def PERSONAL_CONTACT(cls):
                    return cls("PERSONAL_CONTACT")
                
                @schemas.classproperty
                def PERSONAL_PRIVATE(cls):
                    return cls("PERSONAL_PRIVATE")
                
                @schemas.classproperty
                def SENSITIVE_BIRTH(cls):
                    return cls("SENSITIVE_BIRTH")
                
                @schemas.classproperty
                def SENSITIVE_CONTACT(cls):
                    return cls("SENSITIVE_CONTACT")
                
                @schemas.classproperty
                def TIMEOFF(cls):
                    return cls("TIMEOFF")
                
                @schemas.classproperty
                def COMP_CASH(cls):
                    return cls("COMP_CASH")
                
                @schemas.classproperty
                def COMP_EQUITY(cls):
                    return cls("COMP_EQUITY")
                
                @schemas.classproperty
                def SENSITIVE(cls):
                    return cls("SENSITIVE")
                
                @schemas.classproperty
                def PERSONAL(cls):
                    return cls("PERSONAL")
                
                @schemas.classproperty
                def MANAGER(cls):
                    return cls("MANAGER")
                
                @schemas.classproperty
                def GRAND_MANAGER(cls):
                    return cls("GRAND_MANAGER")
                
                @schemas.classproperty
                def DIRECT(cls):
                    return cls("DIRECT")
                
                @schemas.classproperty
                def PEERS(cls):
                    return cls("PEERS")
                
                @schemas.classproperty
                def HIGH(cls):
                    return cls("HIGH")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
            
            
            class targetType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def PERSON(cls):
                    return cls("PERSON")
            targetFilter = schemas.StrSchema
            submitFilter = schemas.StrSchema
            responseReadFilter = schemas.StrSchema
            useFieldAccess = schemas.BoolSchema
            
            
            class approval(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MANAGER(cls):
                    return cls("MANAGER")
                
                @schemas.classproperty
                def GRAND_MANAGER(cls):
                    return cls("GRAND_MANAGER")
            
            
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
            options = schemas.DictSchema
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "orgId": orgId,
                "label": label,
                "fields": fields,
                "blocks": blocks,
                "status": status,
                "type": type,
                "sensitive": sensitive,
                "targetType": targetType,
                "targetFilter": targetFilter,
                "submitFilter": submitFilter,
                "responseReadFilter": responseReadFilter,
                "useFieldAccess": useFieldAccess,
                "approval": approval,
                "authorSensitive": authorSensitive,
                "options": options,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetType"]) -> MetaOapg.properties.targetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetFilter"]) -> MetaOapg.properties.targetFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitFilter"]) -> MetaOapg.properties.submitFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responseReadFilter"]) -> MetaOapg.properties.responseReadFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useFieldAccess"]) -> MetaOapg.properties.useFieldAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval"]) -> MetaOapg.properties.approval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorSensitive"]) -> MetaOapg.properties.authorSensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "orgId", "label", "fields", "blocks", "status", "type", "sensitive", "targetType", "targetFilter", "submitFilter", "responseReadFilter", "useFieldAccess", "approval", "authorSensitive", "options", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union[MetaOapg.properties.fields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blocks"]) -> typing.Union[MetaOapg.properties.blocks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitive"]) -> typing.Union[MetaOapg.properties.sensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetType"]) -> typing.Union[MetaOapg.properties.targetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetFilter"]) -> typing.Union[MetaOapg.properties.targetFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitFilter"]) -> typing.Union[MetaOapg.properties.submitFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responseReadFilter"]) -> typing.Union[MetaOapg.properties.responseReadFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useFieldAccess"]) -> typing.Union[MetaOapg.properties.useFieldAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval"]) -> typing.Union[MetaOapg.properties.approval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorSensitive"]) -> typing.Union[MetaOapg.properties.authorSensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "orgId", "label", "fields", "blocks", "status", "type", "sensitive", "targetType", "targetFilter", "submitFilter", "responseReadFilter", "useFieldAccess", "approval", "authorSensitive", "options", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        fields: typing.Union[MetaOapg.properties.fields, list, tuple, schemas.Unset] = schemas.unset,
        blocks: typing.Union[MetaOapg.properties.blocks, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        sensitive: typing.Union[MetaOapg.properties.sensitive, str, schemas.Unset] = schemas.unset,
        targetType: typing.Union[MetaOapg.properties.targetType, str, schemas.Unset] = schemas.unset,
        targetFilter: typing.Union[MetaOapg.properties.targetFilter, str, schemas.Unset] = schemas.unset,
        submitFilter: typing.Union[MetaOapg.properties.submitFilter, str, schemas.Unset] = schemas.unset,
        responseReadFilter: typing.Union[MetaOapg.properties.responseReadFilter, str, schemas.Unset] = schemas.unset,
        useFieldAccess: typing.Union[MetaOapg.properties.useFieldAccess, bool, schemas.Unset] = schemas.unset,
        approval: typing.Union[MetaOapg.properties.approval, str, schemas.Unset] = schemas.unset,
        authorSensitive: typing.Union[MetaOapg.properties.authorSensitive, str, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PartialForm':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            orgId=orgId,
            label=label,
            fields=fields,
            blocks=blocks,
            status=status,
            type=type,
            sensitive=sensitive,
            targetType=targetType,
            targetFilter=targetFilter,
            submitFilter=submitFilter,
            responseReadFilter=responseReadFilter,
            useFieldAccess=useFieldAccess,
            approval=approval,
            authorSensitive=authorSensitive,
            options=options,
            createId=createId,
            createAt=createAt,
            updateId=updateId,
            updateAt=updateAt,
            deleteId=deleteId,
            deleteAt=deleteAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.form_block import FormBlock
from chart_hop_python_sdk.model.form_field import FormField
