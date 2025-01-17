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


class UserListRow(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "inviteStatus",
            "name",
            "isOrgMember",
        }
        
        class properties:
        
            @staticmethod
            def name() -> typing.Type['Name']:
                return Name
            
            
            class inviteStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INVITED(cls):
                    return cls("INVITED")
                
                @schemas.classproperty
                def JOINED(cls):
                    return cls("JOINED")
                
                @schemas.classproperty
                def NOT_INVITED(cls):
                    return cls("NOT_INVITED")
            isOrgMember = schemas.BoolSchema
            userId = schemas.StrSchema
            personId = schemas.StrSchema
            imagePath = schemas.StrSchema
            email = schemas.StrSchema
            access = schemas.StrSchema
            roleLabel = schemas.StrSchema
            expr = schemas.StrSchema
        
            @staticmethod
            def groupIds() -> typing.Type['UserListRowGroupIds']:
                return UserListRowGroupIds
            loginAt = schemas.Int64Schema
            activeAt = schemas.Int64Schema
            __annotations__ = {
                "name": name,
                "inviteStatus": inviteStatus,
                "isOrgMember": isOrgMember,
                "userId": userId,
                "personId": personId,
                "imagePath": imagePath,
                "email": email,
                "access": access,
                "roleLabel": roleLabel,
                "expr": expr,
                "groupIds": groupIds,
                "loginAt": loginAt,
                "activeAt": activeAt,
            }
    
    inviteStatus: MetaOapg.properties.inviteStatus
    name: 'Name'
    isOrgMember: MetaOapg.properties.isOrgMember
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inviteStatus"]) -> MetaOapg.properties.inviteStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isOrgMember"]) -> MetaOapg.properties.isOrgMember: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personId"]) -> MetaOapg.properties.personId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleLabel"]) -> MetaOapg.properties.roleLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expr"]) -> MetaOapg.properties.expr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupIds"]) -> 'UserListRowGroupIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loginAt"]) -> MetaOapg.properties.loginAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeAt"]) -> MetaOapg.properties.activeAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "inviteStatus", "isOrgMember", "userId", "personId", "imagePath", "email", "access", "roleLabel", "expr", "groupIds", "loginAt", "activeAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inviteStatus"]) -> MetaOapg.properties.inviteStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isOrgMember"]) -> MetaOapg.properties.isOrgMember: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personId"]) -> typing.Union[MetaOapg.properties.personId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleLabel"]) -> typing.Union[MetaOapg.properties.roleLabel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expr"]) -> typing.Union[MetaOapg.properties.expr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupIds"]) -> typing.Union['UserListRowGroupIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loginAt"]) -> typing.Union[MetaOapg.properties.loginAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeAt"]) -> typing.Union[MetaOapg.properties.activeAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "inviteStatus", "isOrgMember", "userId", "personId", "imagePath", "email", "access", "roleLabel", "expr", "groupIds", "loginAt", "activeAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        inviteStatus: typing.Union[MetaOapg.properties.inviteStatus, str, ],
        name: 'Name',
        isOrgMember: typing.Union[MetaOapg.properties.isOrgMember, bool, ],
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        personId: typing.Union[MetaOapg.properties.personId, str, schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        roleLabel: typing.Union[MetaOapg.properties.roleLabel, str, schemas.Unset] = schemas.unset,
        expr: typing.Union[MetaOapg.properties.expr, str, schemas.Unset] = schemas.unset,
        groupIds: typing.Union['UserListRowGroupIds', schemas.Unset] = schemas.unset,
        loginAt: typing.Union[MetaOapg.properties.loginAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activeAt: typing.Union[MetaOapg.properties.activeAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserListRow':
        return super().__new__(
            cls,
            *args,
            inviteStatus=inviteStatus,
            name=name,
            isOrgMember=isOrgMember,
            userId=userId,
            personId=personId,
            imagePath=imagePath,
            email=email,
            access=access,
            roleLabel=roleLabel,
            expr=expr,
            groupIds=groupIds,
            loginAt=loginAt,
            activeAt=activeAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.name import Name
from chart_hop_python_sdk.model.user_list_row_group_ids import UserListRowGroupIds
