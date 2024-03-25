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


class Group(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "aliases",
            "name",
            "id",
            "fields",
            "type",
            "orgId",
            "slug",
        }
        
        class properties:
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            name = schemas.StrSchema
            slug = schemas.StrSchema
        
            @staticmethod
            def aliases() -> typing.Type['GroupAliases']:
                return GroupAliases
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LOCATION(cls):
                    return cls("LOCATION")
                
                @schemas.classproperty
                def DEPARTMENT(cls):
                    return cls("DEPARTMENT")
                
                @schemas.classproperty
                def TEAM(cls):
                    return cls("TEAM")
                
                @schemas.classproperty
                def BAND(cls):
                    return cls("BAND")
                
                @schemas.classproperty
                def JOBCODE(cls):
                    return cls("JOBCODE")
            fields = schemas.DictSchema
            code = schemas.StrSchema
        
            @staticmethod
            def leadJobIds() -> typing.Type['GroupLeadJobIds']:
                return GroupLeadJobIds
        
            @staticmethod
            def address() -> typing.Type['Address']:
                return Address
            level = schemas.Int32Schema
            
            
            class func(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BD(cls):
                    return cls("BD")
                
                @schemas.classproperty
                def CS(cls):
                    return cls("CS")
                
                @schemas.classproperty
                def DESIGN(cls):
                    return cls("DESIGN")
                
                @schemas.classproperty
                def ENGINEERING(cls):
                    return cls("ENGINEERING")
                
                @schemas.classproperty
                def EXECUTIVE(cls):
                    return cls("EXECUTIVE")
                
                @schemas.classproperty
                def FINANCE(cls):
                    return cls("FINANCE")
                
                @schemas.classproperty
                def GENERAL(cls):
                    return cls("GENERAL")
                
                @schemas.classproperty
                def IT(cls):
                    return cls("IT")
                
                @schemas.classproperty
                def LEGAL(cls):
                    return cls("LEGAL")
                
                @schemas.classproperty
                def MARKETING(cls):
                    return cls("MARKETING")
                
                @schemas.classproperty
                def OPERATIONS(cls):
                    return cls("OPERATIONS")
                
                @schemas.classproperty
                def PEOPLE(cls):
                    return cls("PEOPLE")
                
                @schemas.classproperty
                def PRODUCT(cls):
                    return cls("PRODUCT")
                
                @schemas.classproperty
                def RECRUITING(cls):
                    return cls("RECRUITING")
                
                @schemas.classproperty
                def SALES(cls):
                    return cls("SALES")
                
                @schemas.classproperty
                def SECURITY(cls):
                    return cls("SECURITY")
                
                @schemas.classproperty
                def SUPPORT(cls):
                    return cls("SUPPORT")
            
            
            class locationType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OFFICE(cls):
                    return cls("OFFICE")
                
                @schemas.classproperty
                def REMOTE(cls):
                    return cls("REMOTE")
            parentGroupId = schemas.StrSchema
            timezone = schemas.StrSchema
        
            @staticmethod
            def compMin() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def compMax() -> typing.Type['Money']:
                return Money
            
            
            class imagePath(
                schemas.StrSchema
            ):
                pass
            
            
            class color(
                schemas.StrSchema
            ):
                pass
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "orgId": orgId,
                "name": name,
                "slug": slug,
                "aliases": aliases,
                "type": type,
                "fields": fields,
                "code": code,
                "leadJobIds": leadJobIds,
                "address": address,
                "level": level,
                "func": func,
                "locationType": locationType,
                "parentGroupId": parentGroupId,
                "timezone": timezone,
                "compMin": compMin,
                "compMax": compMax,
                "imagePath": imagePath,
                "color": color,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
            }
    
    aliases: 'GroupAliases'
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    fields: MetaOapg.properties.fields
    type: MetaOapg.properties.type
    orgId: MetaOapg.properties.orgId
    slug: MetaOapg.properties.slug
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aliases"]) -> 'GroupAliases': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leadJobIds"]) -> 'GroupLeadJobIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["func"]) -> MetaOapg.properties.func: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationType"]) -> MetaOapg.properties.locationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentGroupId"]) -> MetaOapg.properties.parentGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compMin"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compMax"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "name", "slug", "aliases", "type", "fields", "code", "leadJobIds", "address", "level", "func", "locationType", "parentGroupId", "timezone", "compMin", "compMax", "imagePath", "color", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aliases"]) -> 'GroupAliases': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leadJobIds"]) -> typing.Union['GroupLeadJobIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["func"]) -> typing.Union[MetaOapg.properties.func, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationType"]) -> typing.Union[MetaOapg.properties.locationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentGroupId"]) -> typing.Union[MetaOapg.properties.parentGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compMin"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compMax"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "name", "slug", "aliases", "type", "fields", "code", "leadJobIds", "address", "level", "func", "locationType", "parentGroupId", "timezone", "compMin", "compMax", "imagePath", "color", "createId", "createAt", "updateId", "updateAt", "deleteId", "deleteAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        aliases: 'GroupAliases',
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        fields: typing.Union[MetaOapg.properties.fields, dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, ],
        slug: typing.Union[MetaOapg.properties.slug, str, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        leadJobIds: typing.Union['GroupLeadJobIds', schemas.Unset] = schemas.unset,
        address: typing.Union['Address', schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        func: typing.Union[MetaOapg.properties.func, str, schemas.Unset] = schemas.unset,
        locationType: typing.Union[MetaOapg.properties.locationType, str, schemas.Unset] = schemas.unset,
        parentGroupId: typing.Union[MetaOapg.properties.parentGroupId, str, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        compMin: typing.Union['Money', schemas.Unset] = schemas.unset,
        compMax: typing.Union['Money', schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Group':
        return super().__new__(
            cls,
            *args,
            aliases=aliases,
            name=name,
            id=id,
            fields=fields,
            type=type,
            orgId=orgId,
            slug=slug,
            code=code,
            leadJobIds=leadJobIds,
            address=address,
            level=level,
            func=func,
            locationType=locationType,
            parentGroupId=parentGroupId,
            timezone=timezone,
            compMin=compMin,
            compMax=compMax,
            imagePath=imagePath,
            color=color,
            createId=createId,
            createAt=createAt,
            updateId=updateId,
            updateAt=updateAt,
            deleteId=deleteId,
            deleteAt=deleteAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.address import Address
from chart_hop_python_sdk.model.group_aliases import GroupAliases
from chart_hop_python_sdk.model.group_lead_job_ids import GroupLeadJobIds
from chart_hop_python_sdk.model.money import Money
