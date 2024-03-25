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


class OrgAccess(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "access",
            "orgId",
        }
        
        class properties:
            orgId = schemas.StrSchema
            
            
            class access(
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
            personId = schemas.StrSchema
        
            @staticmethod
            def groupIds() -> typing.Type['OrgAccessGroupIds']:
                return OrgAccessGroupIds
            expr = schemas.StrSchema
            expireAt = schemas.StrSchema
            roleId = schemas.StrSchema
            __annotations__ = {
                "orgId": orgId,
                "access": access,
                "personId": personId,
                "groupIds": groupIds,
                "expr": expr,
                "expireAt": expireAt,
                "roleId": roleId,
            }
    
    access: MetaOapg.properties.access
    orgId: MetaOapg.properties.orgId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personId"]) -> MetaOapg.properties.personId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupIds"]) -> 'OrgAccessGroupIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expr"]) -> MetaOapg.properties.expr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expireAt"]) -> MetaOapg.properties.expireAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleId"]) -> MetaOapg.properties.roleId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["orgId", "access", "personId", "groupIds", "expr", "expireAt", "roleId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personId"]) -> typing.Union[MetaOapg.properties.personId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupIds"]) -> typing.Union['OrgAccessGroupIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expr"]) -> typing.Union[MetaOapg.properties.expr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expireAt"]) -> typing.Union[MetaOapg.properties.expireAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleId"]) -> typing.Union[MetaOapg.properties.roleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["orgId", "access", "personId", "groupIds", "expr", "expireAt", "roleId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access: typing.Union[MetaOapg.properties.access, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, ],
        personId: typing.Union[MetaOapg.properties.personId, str, schemas.Unset] = schemas.unset,
        groupIds: typing.Union['OrgAccessGroupIds', schemas.Unset] = schemas.unset,
        expr: typing.Union[MetaOapg.properties.expr, str, schemas.Unset] = schemas.unset,
        expireAt: typing.Union[MetaOapg.properties.expireAt, str, schemas.Unset] = schemas.unset,
        roleId: typing.Union[MetaOapg.properties.roleId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrgAccess':
        return super().__new__(
            cls,
            *args,
            access=access,
            orgId=orgId,
            personId=personId,
            groupIds=groupIds,
            expr=expr,
            expireAt=expireAt,
            roleId=roleId,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.org_access_group_ids import OrgAccessGroupIds
