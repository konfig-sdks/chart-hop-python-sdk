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


class User(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def name() -> typing.Type['Name']:
                return Name
            title = schemas.StrSchema
            appId = schemas.StrSchema
            email = schemas.StrSchema
            password = schemas.StrSchema
            
            
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
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USER(cls):
                    return cls("USER")
                
                @schemas.classproperty
                def APP(cls):
                    return cls("APP")
            options = schemas.DictSchema
            internalOptions = schemas.DictSchema
        
            @staticmethod
            def bundleInstall() -> typing.Type['BundleInstall']:
                return BundleInstall
            secrets = schemas.DictSchema
            activeAt = schemas.StrSchema
            loginAt = schemas.StrSchema
            loginFailCount = schemas.Int32Schema
            remoteIp = schemas.StrSchema
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            verifyAt = schemas.StrSchema
            
            
            class mfas(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WebRegisteredCredential']:
                        return WebRegisteredCredential
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WebRegisteredCredential'], typing.List['WebRegisteredCredential']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mfas':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WebRegisteredCredential':
                    return super().__getitem__(i)
            
            
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
                "id": id,
                "name": name,
                "title": title,
                "appId": appId,
                "email": email,
                "password": password,
                "orgs": orgs,
                "imagePath": imagePath,
                "status": status,
                "type": type,
                "options": options,
                "internalOptions": internalOptions,
                "bundleInstall": bundleInstall,
                "secrets": secrets,
                "activeAt": activeAt,
                "loginAt": loginAt,
                "loginFailCount": loginFailCount,
                "remoteIp": remoteIp,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "verifyAt": verifyAt,
                "mfas": mfas,
                "emailSettings": emailSettings,
            }
    
    name: 'Name'
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgs"]) -> MetaOapg.properties.orgs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalOptions"]) -> MetaOapg.properties.internalOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bundleInstall"]) -> 'BundleInstall': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secrets"]) -> MetaOapg.properties.secrets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeAt"]) -> MetaOapg.properties.activeAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loginAt"]) -> MetaOapg.properties.loginAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loginFailCount"]) -> MetaOapg.properties.loginFailCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remoteIp"]) -> MetaOapg.properties.remoteIp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verifyAt"]) -> MetaOapg.properties.verifyAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mfas"]) -> MetaOapg.properties.mfas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailSettings"]) -> MetaOapg.properties.emailSettings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "title", "appId", "email", "password", "orgs", "imagePath", "status", "type", "options", "internalOptions", "bundleInstall", "secrets", "activeAt", "loginAt", "loginFailCount", "remoteIp", "createId", "createAt", "updateId", "updateAt", "verifyAt", "mfas", "emailSettings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> typing.Union[MetaOapg.properties.appId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgs"]) -> typing.Union[MetaOapg.properties.orgs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalOptions"]) -> typing.Union[MetaOapg.properties.internalOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bundleInstall"]) -> typing.Union['BundleInstall', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secrets"]) -> typing.Union[MetaOapg.properties.secrets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeAt"]) -> typing.Union[MetaOapg.properties.activeAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loginAt"]) -> typing.Union[MetaOapg.properties.loginAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loginFailCount"]) -> typing.Union[MetaOapg.properties.loginFailCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remoteIp"]) -> typing.Union[MetaOapg.properties.remoteIp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createId"]) -> typing.Union[MetaOapg.properties.createId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> typing.Union[MetaOapg.properties.createAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> typing.Union[MetaOapg.properties.updateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> typing.Union[MetaOapg.properties.updateAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verifyAt"]) -> typing.Union[MetaOapg.properties.verifyAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mfas"]) -> typing.Union[MetaOapg.properties.mfas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailSettings"]) -> typing.Union[MetaOapg.properties.emailSettings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "title", "appId", "email", "password", "orgs", "imagePath", "status", "type", "options", "internalOptions", "bundleInstall", "secrets", "activeAt", "loginAt", "loginFailCount", "remoteIp", "createId", "createAt", "updateId", "updateAt", "verifyAt", "mfas", "emailSettings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: 'Name',
        id: typing.Union[MetaOapg.properties.id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        appId: typing.Union[MetaOapg.properties.appId, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        orgs: typing.Union[MetaOapg.properties.orgs, list, tuple, schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        internalOptions: typing.Union[MetaOapg.properties.internalOptions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        bundleInstall: typing.Union['BundleInstall', schemas.Unset] = schemas.unset,
        secrets: typing.Union[MetaOapg.properties.secrets, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        activeAt: typing.Union[MetaOapg.properties.activeAt, str, schemas.Unset] = schemas.unset,
        loginAt: typing.Union[MetaOapg.properties.loginAt, str, schemas.Unset] = schemas.unset,
        loginFailCount: typing.Union[MetaOapg.properties.loginFailCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        remoteIp: typing.Union[MetaOapg.properties.remoteIp, str, schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        verifyAt: typing.Union[MetaOapg.properties.verifyAt, str, schemas.Unset] = schemas.unset,
        mfas: typing.Union[MetaOapg.properties.mfas, list, tuple, schemas.Unset] = schemas.unset,
        emailSettings: typing.Union[MetaOapg.properties.emailSettings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *args,
            name=name,
            id=id,
            title=title,
            appId=appId,
            email=email,
            password=password,
            orgs=orgs,
            imagePath=imagePath,
            status=status,
            type=type,
            options=options,
            internalOptions=internalOptions,
            bundleInstall=bundleInstall,
            secrets=secrets,
            activeAt=activeAt,
            loginAt=loginAt,
            loginFailCount=loginFailCount,
            remoteIp=remoteIp,
            createId=createId,
            createAt=createAt,
            updateId=updateId,
            updateAt=updateAt,
            verifyAt=verifyAt,
            mfas=mfas,
            emailSettings=emailSettings,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.bundle_install import BundleInstall
from chart_hop_python_sdk.model.name import Name
from chart_hop_python_sdk.model.org_access import OrgAccess
from chart_hop_python_sdk.model.user_email_setting import UserEmailSetting
from chart_hop_python_sdk.model.web_registered_credential import WebRegisteredCredential
