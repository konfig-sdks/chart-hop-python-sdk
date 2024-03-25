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


class UpdateUser(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            appId = schemas.StrSchema
        
            @staticmethod
            def name() -> typing.Type['Name']:
                return Name
            email = schemas.StrSchema
            
            
            class orgs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OrgAccess']:
                        return OrgAccess
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OrgAccess'], typing.List['OrgAccess']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'orgs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OrgAccess':
                    return super().__getitem__(i)
            
            
            class imagePath(
                schemas.StrSchema
            ):
                pass
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SUPERUSER(cls):
                    return cls("SUPERUSER")
                
                @schemas.classproperty
                def NORMAL(cls):
                    return cls("NORMAL")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def UNINSTALLED(cls):
                    return cls("UNINSTALLED")
            options = schemas.DictSchema
            internalOptions = schemas.DictSchema
            secrets = schemas.DictSchema
            
            
            class emailSettings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserEmailSetting']:
                        return UserEmailSetting
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserEmailSetting'], typing.List['UserEmailSetting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emailSettings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserEmailSetting':
                    return super().__getitem__(i)
            __annotations__ = {
                "appId": appId,
                "name": name,
                "email": email,
                "orgs": orgs,
                "imagePath": imagePath,
                "status": status,
                "options": options,
                "internalOptions": internalOptions,
                "secrets": secrets,
                "emailSettings": emailSettings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgs"]) -> MetaOapg.properties.orgs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalOptions"]) -> MetaOapg.properties.internalOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secrets"]) -> MetaOapg.properties.secrets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailSettings"]) -> MetaOapg.properties.emailSettings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appId", "name", "email", "orgs", "imagePath", "status", "options", "internalOptions", "secrets", "emailSettings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> typing.Union[MetaOapg.properties.appId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['Name', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgs"]) -> typing.Union[MetaOapg.properties.orgs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalOptions"]) -> typing.Union[MetaOapg.properties.internalOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secrets"]) -> typing.Union[MetaOapg.properties.secrets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailSettings"]) -> typing.Union[MetaOapg.properties.emailSettings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appId", "name", "email", "orgs", "imagePath", "status", "options", "internalOptions", "secrets", "emailSettings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        appId: typing.Union[MetaOapg.properties.appId, str, schemas.Unset] = schemas.unset,
        name: typing.Union['Name', schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        orgs: typing.Union[MetaOapg.properties.orgs, list, tuple, schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        internalOptions: typing.Union[MetaOapg.properties.internalOptions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        secrets: typing.Union[MetaOapg.properties.secrets, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        emailSettings: typing.Union[MetaOapg.properties.emailSettings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateUser':
        return super().__new__(
            cls,
            *args,
            appId=appId,
            name=name,
            email=email,
            orgs=orgs,
            imagePath=imagePath,
            status=status,
            options=options,
            internalOptions=internalOptions,
            secrets=secrets,
            emailSettings=emailSettings,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.name import Name
from chart_hop_python_sdk.model.org_access import OrgAccess
from chart_hop_python_sdk.model.user_email_setting import UserEmailSetting
