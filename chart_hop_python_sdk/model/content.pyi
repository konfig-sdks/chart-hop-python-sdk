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


class Content(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "updateId",
            "createId",
            "updateAt",
            "id",
            "sensitive",
            "title",
            "createAt",
            "orgId",
        }
        
        class properties:
            title = schemas.StrSchema
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            
            
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
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            parentContentId = schemas.StrSchema
            path = schemas.StrSchema
            
            
            class blocks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ContentBlock']:
                        return ContentBlock
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ContentBlock'], typing.List['ContentBlock']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'blocks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContentBlock':
                    return super().__getitem__(i)
            
            
            class imagePath(
                schemas.StrSchema
            ):
                pass
            emoji = schemas.StrSchema
            
            
            class coverImagePath(
                schemas.StrSchema
            ):
                pass
            
            
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
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("DRAFT")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def ARCHIVED(cls):
                    return cls("ARCHIVED")
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "id": id,
                "orgId": orgId,
                "sensitive": sensitive,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "parentContentId": parentContentId,
                "path": path,
                "blocks": blocks,
                "imagePath": imagePath,
                "emoji": emoji,
                "coverImagePath": coverImagePath,
                "shareAccess": shareAccess,
                "status": status,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
            }
    
    updateId: MetaOapg.properties.updateId
    createId: MetaOapg.properties.createId
    updateAt: MetaOapg.properties.updateAt
    id: MetaOapg.properties.id
    sensitive: MetaOapg.properties.sensitive
    title: MetaOapg.properties.title
    createAt: MetaOapg.properties.createAt
    orgId: MetaOapg.properties.orgId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentContentId"]) -> MetaOapg.properties.parentContentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emoji"]) -> MetaOapg.properties.emoji: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverImagePath"]) -> MetaOapg.properties.coverImagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteId"]) -> MetaOapg.properties.deleteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteAt"]) -> MetaOapg.properties.deleteAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "orgId", "sensitive", "createId", "createAt", "updateId", "updateAt", "parentContentId", "path", "blocks", "imagePath", "emoji", "coverImagePath", "shareAccess", "status", "deleteId", "deleteAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentContentId"]) -> typing.Union[MetaOapg.properties.parentContentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blocks"]) -> typing.Union[MetaOapg.properties.blocks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emoji"]) -> typing.Union[MetaOapg.properties.emoji, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverImagePath"]) -> typing.Union[MetaOapg.properties.coverImagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteId"]) -> typing.Union[MetaOapg.properties.deleteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteAt"]) -> typing.Union[MetaOapg.properties.deleteAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "orgId", "sensitive", "createId", "createAt", "updateId", "updateAt", "parentContentId", "path", "blocks", "imagePath", "emoji", "coverImagePath", "shareAccess", "status", "deleteId", "deleteAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updateId: typing.Union[MetaOapg.properties.updateId, str, ],
        createId: typing.Union[MetaOapg.properties.createId, str, ],
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        sensitive: typing.Union[MetaOapg.properties.sensitive, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        createAt: typing.Union[MetaOapg.properties.createAt, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, ],
        parentContentId: typing.Union[MetaOapg.properties.parentContentId, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        blocks: typing.Union[MetaOapg.properties.blocks, list, tuple, schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        emoji: typing.Union[MetaOapg.properties.emoji, str, schemas.Unset] = schemas.unset,
        coverImagePath: typing.Union[MetaOapg.properties.coverImagePath, str, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Content':
        return super().__new__(
            cls,
            *args,
            updateId=updateId,
            createId=createId,
            updateAt=updateAt,
            id=id,
            sensitive=sensitive,
            title=title,
            createAt=createAt,
            orgId=orgId,
            parentContentId=parentContentId,
            path=path,
            blocks=blocks,
            imagePath=imagePath,
            emoji=emoji,
            coverImagePath=coverImagePath,
            shareAccess=shareAccess,
            status=status,
            deleteId=deleteId,
            deleteAt=deleteAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.content_block import ContentBlock
from chart_hop_python_sdk.model.share_access import ShareAccess