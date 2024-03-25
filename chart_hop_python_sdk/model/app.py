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


class App(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "summary",
            "name",
            "id",
            "title",
            "minAccess",
            "orgId",
            "status",
        }
        
        class properties:
            summary = schemas.StrSchema
            title = schemas.StrSchema
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[a-z0-9-]+$',
                    }]
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "GLOBAL": "GLOBAL",
                        "ACTIVE": "ACTIVE",
                        "INACTIVE": "INACTIVE",
                        "DEVELOPMENT": "DEVELOPMENT",
                    }
                
                @schemas.classproperty
                def GLOBAL(cls):
                    return cls("GLOBAL")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def DEVELOPMENT(cls):
                    return cls("DEVELOPMENT")
            
            
            class minAccess(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NONE": "NONE",
                        "VIEW": "VIEW",
                        "LIMITED": "LIMITED",
                        "MEMBER_LIMITED_COMP": "MEMBER_LIMITED_COMP",
                        "MEMBER": "MEMBER",
                        "CUSTOM": "CUSTOM",
                        "TECH_OWNER": "TECH_OWNER",
                        "TIMEOFF": "TIMEOFF",
                        "CONTACT": "CONTACT",
                        "COMP_CASH": "COMP_CASH",
                        "COMP_EQUITY": "COMP_EQUITY",
                        "COMP_ALL": "COMP_ALL",
                        "RECRUIT_SENSITIVE": "RECRUIT_SENSITIVE",
                        "RECRUIT_PRIMARY": "RECRUIT_PRIMARY",
                        "SENSITIVE_LIMITED_COMP": "SENSITIVE_LIMITED_COMP",
                        "SENSITIVE": "SENSITIVE",
                        "PRIMARY": "PRIMARY",
                        "PEOPLE_OPS_ADMIN": "PEOPLE_OPS_ADMIN",
                        "PEOPLE_OPS_ADMIN_NO_COMP_DATA": "PEOPLE_OPS_ADMIN_NO_COMP_DATA",
                        "PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA": "PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA",
                        "OWNER": "OWNER",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def VIEW(cls):
                    return cls("VIEW")
                
                @schemas.classproperty
                def LIMITED(cls):
                    return cls("LIMITED")
                
                @schemas.classproperty
                def MEMBER_LIMITED_COMP(cls):
                    return cls("MEMBER_LIMITED_COMP")
                
                @schemas.classproperty
                def MEMBER(cls):
                    return cls("MEMBER")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("CUSTOM")
                
                @schemas.classproperty
                def TECH_OWNER(cls):
                    return cls("TECH_OWNER")
                
                @schemas.classproperty
                def TIMEOFF(cls):
                    return cls("TIMEOFF")
                
                @schemas.classproperty
                def CONTACT(cls):
                    return cls("CONTACT")
                
                @schemas.classproperty
                def COMP_CASH(cls):
                    return cls("COMP_CASH")
                
                @schemas.classproperty
                def COMP_EQUITY(cls):
                    return cls("COMP_EQUITY")
                
                @schemas.classproperty
                def COMP_ALL(cls):
                    return cls("COMP_ALL")
                
                @schemas.classproperty
                def RECRUIT_SENSITIVE(cls):
                    return cls("RECRUIT_SENSITIVE")
                
                @schemas.classproperty
                def RECRUIT_PRIMARY(cls):
                    return cls("RECRUIT_PRIMARY")
                
                @schemas.classproperty
                def SENSITIVE_LIMITED_COMP(cls):
                    return cls("SENSITIVE_LIMITED_COMP")
                
                @schemas.classproperty
                def SENSITIVE(cls):
                    return cls("SENSITIVE")
                
                @schemas.classproperty
                def PRIMARY(cls):
                    return cls("PRIMARY")
                
                @schemas.classproperty
                def PEOPLE_OPS_ADMIN(cls):
                    return cls("PEOPLE_OPS_ADMIN")
                
                @schemas.classproperty
                def PEOPLE_OPS_ADMIN_NO_COMP_DATA(cls):
                    return cls("PEOPLE_OPS_ADMIN_NO_COMP_DATA")
                
                @schemas.classproperty
                def PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA(cls):
                    return cls("PEOPLE_OPS_ADMIN_NO_SENSITIVE_DATA")
                
                @schemas.classproperty
                def OWNER(cls):
                    return cls("OWNER")
        
            @staticmethod
            def tags() -> typing.Type['AppTags']:
                return AppTags
            description = schemas.StrSchema
        
            @staticmethod
            def redirectUris() -> typing.Type['AppRedirectUris']:
                return AppRedirectUris
        
            @staticmethod
            def allowedIps() -> typing.Type['AppAllowedIps']:
                return AppAllowedIps
            
            
            class configFields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppConfigField']:
                        return AppConfigField
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppConfigField'], typing.List['AppConfigField']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'configFields':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppConfigField':
                    return super().__getitem__(i)
            setupInstructions = schemas.StrSchema
            cronOrder = schemas.Int32Schema
            
            
            class cronSchedule(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DAILY": "DAILY",
                        "WEEKLY": "WEEKLY",
                    }
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("DAILY")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("WEEKLY")
            
            
            class cronDayOfWeek(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "MONDAY": "MONDAY",
                        "TUESDAY": "TUESDAY",
                        "WEDNESDAY": "WEDNESDAY",
                        "THURSDAY": "THURSDAY",
                        "FRIDAY": "FRIDAY",
                        "SATURDAY": "SATURDAY",
                        "SUNDAY": "SUNDAY",
                    }
                
                @schemas.classproperty
                def MONDAY(cls):
                    return cls("MONDAY")
                
                @schemas.classproperty
                def TUESDAY(cls):
                    return cls("TUESDAY")
                
                @schemas.classproperty
                def WEDNESDAY(cls):
                    return cls("WEDNESDAY")
                
                @schemas.classproperty
                def THURSDAY(cls):
                    return cls("THURSDAY")
                
                @schemas.classproperty
                def FRIDAY(cls):
                    return cls("FRIDAY")
                
                @schemas.classproperty
                def SATURDAY(cls):
                    return cls("SATURDAY")
                
                @schemas.classproperty
                def SUNDAY(cls):
                    return cls("SUNDAY")
            
            
            class imagePath(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9._/-]+$',
                    }]
            
            
            class wordmarkImagePath(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9._/-]+$',
                    }]
            
            
            class poweredByImagePath(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9._/-]+$',
                    }]
            roleId = schemas.StrSchema
            eventNotifyUrl = schemas.StrSchema
        
            @staticmethod
            def payload() -> typing.Type['AppPayload']:
                return AppPayload
        
            @staticmethod
            def events() -> typing.Type['AppEvents']:
                return AppEvents
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "APP": "APP",
                        "BUNDLE": "BUNDLE",
                        "INTERNAL": "INTERNAL",
                    }
                
                @schemas.classproperty
                def APP(cls):
                    return cls("APP")
                
                @schemas.classproperty
                def BUNDLE(cls):
                    return cls("BUNDLE")
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("INTERNAL")
        
            @staticmethod
            def bundle() -> typing.Type['Bundle']:
                return Bundle
        
            @staticmethod
            def scopes() -> typing.Type['AppScopes']:
                return AppScopes
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
            __annotations__ = {
                "summary": summary,
                "title": title,
                "id": id,
                "orgId": orgId,
                "name": name,
                "status": status,
                "minAccess": minAccess,
                "tags": tags,
                "description": description,
                "redirectUris": redirectUris,
                "allowedIps": allowedIps,
                "configFields": configFields,
                "setupInstructions": setupInstructions,
                "cronOrder": cronOrder,
                "cronSchedule": cronSchedule,
                "cronDayOfWeek": cronDayOfWeek,
                "imagePath": imagePath,
                "wordmarkImagePath": wordmarkImagePath,
                "poweredByImagePath": poweredByImagePath,
                "roleId": roleId,
                "eventNotifyUrl": eventNotifyUrl,
                "payload": payload,
                "events": events,
                "type": type,
                "bundle": bundle,
                "scopes": scopes,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
            }
    
    summary: MetaOapg.properties.summary
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    minAccess: MetaOapg.properties.minAccess
    orgId: MetaOapg.properties.orgId
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minAccess"]) -> MetaOapg.properties.minAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'AppTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirectUris"]) -> 'AppRedirectUris': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedIps"]) -> 'AppAllowedIps': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configFields"]) -> MetaOapg.properties.configFields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["setupInstructions"]) -> MetaOapg.properties.setupInstructions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cronOrder"]) -> MetaOapg.properties.cronOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cronSchedule"]) -> MetaOapg.properties.cronSchedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cronDayOfWeek"]) -> MetaOapg.properties.cronDayOfWeek: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wordmarkImagePath"]) -> MetaOapg.properties.wordmarkImagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["poweredByImagePath"]) -> MetaOapg.properties.poweredByImagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleId"]) -> MetaOapg.properties.roleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventNotifyUrl"]) -> MetaOapg.properties.eventNotifyUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> 'AppPayload': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'AppEvents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bundle"]) -> 'Bundle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> 'AppScopes': ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "title", "id", "orgId", "name", "status", "minAccess", "tags", "description", "redirectUris", "allowedIps", "configFields", "setupInstructions", "cronOrder", "cronSchedule", "cronDayOfWeek", "imagePath", "wordmarkImagePath", "poweredByImagePath", "roleId", "eventNotifyUrl", "payload", "events", "type", "bundle", "scopes", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minAccess"]) -> MetaOapg.properties.minAccess: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['AppTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirectUris"]) -> typing.Union['AppRedirectUris', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedIps"]) -> typing.Union['AppAllowedIps', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configFields"]) -> typing.Union[MetaOapg.properties.configFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["setupInstructions"]) -> typing.Union[MetaOapg.properties.setupInstructions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cronOrder"]) -> typing.Union[MetaOapg.properties.cronOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cronSchedule"]) -> typing.Union[MetaOapg.properties.cronSchedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cronDayOfWeek"]) -> typing.Union[MetaOapg.properties.cronDayOfWeek, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wordmarkImagePath"]) -> typing.Union[MetaOapg.properties.wordmarkImagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["poweredByImagePath"]) -> typing.Union[MetaOapg.properties.poweredByImagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleId"]) -> typing.Union[MetaOapg.properties.roleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventNotifyUrl"]) -> typing.Union[MetaOapg.properties.eventNotifyUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> typing.Union['AppPayload', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union['AppEvents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bundle"]) -> typing.Union['Bundle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> typing.Union['AppScopes', schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "title", "id", "orgId", "name", "status", "minAccess", "tags", "description", "redirectUris", "allowedIps", "configFields", "setupInstructions", "cronOrder", "cronSchedule", "cronDayOfWeek", "imagePath", "wordmarkImagePath", "poweredByImagePath", "roleId", "eventNotifyUrl", "payload", "events", "type", "bundle", "scopes", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        summary: typing.Union[MetaOapg.properties.summary, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        minAccess: typing.Union[MetaOapg.properties.minAccess, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        tags: typing.Union['AppTags', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        redirectUris: typing.Union['AppRedirectUris', schemas.Unset] = schemas.unset,
        allowedIps: typing.Union['AppAllowedIps', schemas.Unset] = schemas.unset,
        configFields: typing.Union[MetaOapg.properties.configFields, list, tuple, schemas.Unset] = schemas.unset,
        setupInstructions: typing.Union[MetaOapg.properties.setupInstructions, str, schemas.Unset] = schemas.unset,
        cronOrder: typing.Union[MetaOapg.properties.cronOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cronSchedule: typing.Union[MetaOapg.properties.cronSchedule, str, schemas.Unset] = schemas.unset,
        cronDayOfWeek: typing.Union[MetaOapg.properties.cronDayOfWeek, str, schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        wordmarkImagePath: typing.Union[MetaOapg.properties.wordmarkImagePath, str, schemas.Unset] = schemas.unset,
        poweredByImagePath: typing.Union[MetaOapg.properties.poweredByImagePath, str, schemas.Unset] = schemas.unset,
        roleId: typing.Union[MetaOapg.properties.roleId, str, schemas.Unset] = schemas.unset,
        eventNotifyUrl: typing.Union[MetaOapg.properties.eventNotifyUrl, str, schemas.Unset] = schemas.unset,
        payload: typing.Union['AppPayload', schemas.Unset] = schemas.unset,
        events: typing.Union['AppEvents', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        bundle: typing.Union['Bundle', schemas.Unset] = schemas.unset,
        scopes: typing.Union['AppScopes', schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'App':
        return super().__new__(
            cls,
            *args,
            summary=summary,
            name=name,
            id=id,
            title=title,
            minAccess=minAccess,
            orgId=orgId,
            status=status,
            tags=tags,
            description=description,
            redirectUris=redirectUris,
            allowedIps=allowedIps,
            configFields=configFields,
            setupInstructions=setupInstructions,
            cronOrder=cronOrder,
            cronSchedule=cronSchedule,
            cronDayOfWeek=cronDayOfWeek,
            imagePath=imagePath,
            wordmarkImagePath=wordmarkImagePath,
            poweredByImagePath=poweredByImagePath,
            roleId=roleId,
            eventNotifyUrl=eventNotifyUrl,
            payload=payload,
            events=events,
            type=type,
            bundle=bundle,
            scopes=scopes,
            createId=createId,
            createAt=createAt,
            updateId=updateId,
            updateAt=updateAt,
            deleteId=deleteId,
            deleteAt=deleteAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.app_allowed_ips import AppAllowedIps
from chart_hop_python_sdk.model.app_config_field import AppConfigField
from chart_hop_python_sdk.model.app_events import AppEvents
from chart_hop_python_sdk.model.app_payload import AppPayload
from chart_hop_python_sdk.model.app_redirect_uris import AppRedirectUris
from chart_hop_python_sdk.model.app_scopes import AppScopes
from chart_hop_python_sdk.model.app_tags import AppTags
from chart_hop_python_sdk.model.bundle import Bundle
