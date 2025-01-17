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


class Org(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "id",
            "slug",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            slug = schemas.StrSchema
            customerId = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PRIVATE": "PRIVATE",
                        "PUBLIC": "PUBLIC",
                        "EDU": "EDU",
                        "GOV": "GOV",
                        "NONPROFIT": "NONPROFIT",
                        "DEMO": "DEMO",
                        "TEST": "TEST",
                    }
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("PUBLIC")
                
                @schemas.classproperty
                def EDU(cls):
                    return cls("EDU")
                
                @schemas.classproperty
                def GOV(cls):
                    return cls("GOV")
                
                @schemas.classproperty
                def NONPROFIT(cls):
                    return cls("NONPROFIT")
                
                @schemas.classproperty
                def DEMO(cls):
                    return cls("DEMO")
                
                @schemas.classproperty
                def TEST(cls):
                    return cls("TEST")
            industry = schemas.StrSchema
            estEmployees = schemas.Int32Schema
            estRevenue = schemas.Int32Schema
            foundedYear = schemas.Int32Schema
        
            @staticmethod
            def address() -> typing.Type['Address']:
                return Address
            
            
            class phone(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^\+?[1-9]\d{1,14}$',
                    }]
            email = schemas.StrSchema
            url = schemas.StrSchema
            
            
            class domains(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OrgDomain']:
                        return OrgDomain
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OrgDomain'], typing.List['OrgDomain']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'domains':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OrgDomain':
                    return super().__getitem__(i)
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTIVE": "ACTIVE",
                        "INACTIVE": "INACTIVE",
                        "DISABLED": "DISABLED",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def DISABLED(cls):
                    return cls("DISABLED")
            
            
            class imagePath(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9._/-]+$',
                    }]
        
            @staticmethod
            def currencies() -> typing.Type['OrgCurrencies']:
                return OrgCurrencies
            stock = schemas.StrSchema
            timezone = schemas.StrSchema
            appTime = schemas.StrSchema
            zone = schemas.Int32Schema
            fiscalStart = schemas.Int32Schema
            headJobId = schemas.StrSchema
            startDate = schemas.StrSchema
            sensitiveFields = schemas.DictSchema
            options = schemas.DictSchema
            internalOptions = schemas.DictSchema
            
            
            class onboardSteps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OnboardStepResult']:
                        return OnboardStepResult
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OnboardStepResult'], typing.List['OnboardStepResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'onboardSteps':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OnboardStepResult':
                    return super().__getitem__(i)
            onboarding = schemas.BoolSchema
            selfServeImporting = schemas.BoolSchema
            headCount = schemas.Int32Schema
            userCount = schemas.Int32Schema
            activeUserCount = schemas.Int32Schema
            activeAt = schemas.StrSchema
            changeAt = schemas.StrSchema
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            destroyAt = schemas.StrSchema
            destroyId = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "slug": slug,
                "customerId": customerId,
                "type": type,
                "industry": industry,
                "estEmployees": estEmployees,
                "estRevenue": estRevenue,
                "foundedYear": foundedYear,
                "address": address,
                "phone": phone,
                "email": email,
                "url": url,
                "domains": domains,
                "status": status,
                "imagePath": imagePath,
                "currencies": currencies,
                "stock": stock,
                "timezone": timezone,
                "appTime": appTime,
                "zone": zone,
                "fiscalStart": fiscalStart,
                "headJobId": headJobId,
                "startDate": startDate,
                "sensitiveFields": sensitiveFields,
                "options": options,
                "internalOptions": internalOptions,
                "onboardSteps": onboardSteps,
                "onboarding": onboarding,
                "selfServeImporting": selfServeImporting,
                "headCount": headCount,
                "userCount": userCount,
                "activeUserCount": activeUserCount,
                "activeAt": activeAt,
                "changeAt": changeAt,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "destroyAt": destroyAt,
                "destroyId": destroyId,
            }
    
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    slug: MetaOapg.properties.slug
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["industry"]) -> MetaOapg.properties.industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estEmployees"]) -> MetaOapg.properties.estEmployees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estRevenue"]) -> MetaOapg.properties.estRevenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foundedYear"]) -> MetaOapg.properties.foundedYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domains"]) -> MetaOapg.properties.domains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePath"]) -> MetaOapg.properties.imagePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencies"]) -> 'OrgCurrencies': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stock"]) -> MetaOapg.properties.stock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appTime"]) -> MetaOapg.properties.appTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zone"]) -> MetaOapg.properties.zone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fiscalStart"]) -> MetaOapg.properties.fiscalStart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headJobId"]) -> MetaOapg.properties.headJobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitiveFields"]) -> MetaOapg.properties.sensitiveFields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalOptions"]) -> MetaOapg.properties.internalOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboardSteps"]) -> MetaOapg.properties.onboardSteps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboarding"]) -> MetaOapg.properties.onboarding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfServeImporting"]) -> MetaOapg.properties.selfServeImporting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headCount"]) -> MetaOapg.properties.headCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userCount"]) -> MetaOapg.properties.userCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeUserCount"]) -> MetaOapg.properties.activeUserCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeAt"]) -> MetaOapg.properties.activeAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changeAt"]) -> MetaOapg.properties.changeAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destroyAt"]) -> MetaOapg.properties.destroyAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destroyId"]) -> MetaOapg.properties.destroyId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "slug", "customerId", "type", "industry", "estEmployees", "estRevenue", "foundedYear", "address", "phone", "email", "url", "domains", "status", "imagePath", "currencies", "stock", "timezone", "appTime", "zone", "fiscalStart", "headJobId", "startDate", "sensitiveFields", "options", "internalOptions", "onboardSteps", "onboarding", "selfServeImporting", "headCount", "userCount", "activeUserCount", "activeAt", "changeAt", "createId", "createAt", "updateId", "updateAt", "destroyAt", "destroyId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> typing.Union[MetaOapg.properties.customerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["industry"]) -> typing.Union[MetaOapg.properties.industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estEmployees"]) -> typing.Union[MetaOapg.properties.estEmployees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estRevenue"]) -> typing.Union[MetaOapg.properties.estRevenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foundedYear"]) -> typing.Union[MetaOapg.properties.foundedYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domains"]) -> typing.Union[MetaOapg.properties.domains, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePath"]) -> typing.Union[MetaOapg.properties.imagePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencies"]) -> typing.Union['OrgCurrencies', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stock"]) -> typing.Union[MetaOapg.properties.stock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appTime"]) -> typing.Union[MetaOapg.properties.appTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zone"]) -> typing.Union[MetaOapg.properties.zone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fiscalStart"]) -> typing.Union[MetaOapg.properties.fiscalStart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headJobId"]) -> typing.Union[MetaOapg.properties.headJobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitiveFields"]) -> typing.Union[MetaOapg.properties.sensitiveFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalOptions"]) -> typing.Union[MetaOapg.properties.internalOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboardSteps"]) -> typing.Union[MetaOapg.properties.onboardSteps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboarding"]) -> typing.Union[MetaOapg.properties.onboarding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selfServeImporting"]) -> typing.Union[MetaOapg.properties.selfServeImporting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headCount"]) -> typing.Union[MetaOapg.properties.headCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userCount"]) -> typing.Union[MetaOapg.properties.userCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeUserCount"]) -> typing.Union[MetaOapg.properties.activeUserCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeAt"]) -> typing.Union[MetaOapg.properties.activeAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changeAt"]) -> typing.Union[MetaOapg.properties.changeAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createId"]) -> typing.Union[MetaOapg.properties.createId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> typing.Union[MetaOapg.properties.createAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> typing.Union[MetaOapg.properties.updateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> typing.Union[MetaOapg.properties.updateAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destroyAt"]) -> typing.Union[MetaOapg.properties.destroyAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destroyId"]) -> typing.Union[MetaOapg.properties.destroyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "slug", "customerId", "type", "industry", "estEmployees", "estRevenue", "foundedYear", "address", "phone", "email", "url", "domains", "status", "imagePath", "currencies", "stock", "timezone", "appTime", "zone", "fiscalStart", "headJobId", "startDate", "sensitiveFields", "options", "internalOptions", "onboardSteps", "onboarding", "selfServeImporting", "headCount", "userCount", "activeUserCount", "activeAt", "changeAt", "createId", "createAt", "updateId", "updateAt", "destroyAt", "destroyId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        slug: typing.Union[MetaOapg.properties.slug, str, ],
        customerId: typing.Union[MetaOapg.properties.customerId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        industry: typing.Union[MetaOapg.properties.industry, str, schemas.Unset] = schemas.unset,
        estEmployees: typing.Union[MetaOapg.properties.estEmployees, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        estRevenue: typing.Union[MetaOapg.properties.estRevenue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        foundedYear: typing.Union[MetaOapg.properties.foundedYear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        address: typing.Union['Address', schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        domains: typing.Union[MetaOapg.properties.domains, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        imagePath: typing.Union[MetaOapg.properties.imagePath, str, schemas.Unset] = schemas.unset,
        currencies: typing.Union['OrgCurrencies', schemas.Unset] = schemas.unset,
        stock: typing.Union[MetaOapg.properties.stock, str, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        appTime: typing.Union[MetaOapg.properties.appTime, str, schemas.Unset] = schemas.unset,
        zone: typing.Union[MetaOapg.properties.zone, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fiscalStart: typing.Union[MetaOapg.properties.fiscalStart, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        headJobId: typing.Union[MetaOapg.properties.headJobId, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, schemas.Unset] = schemas.unset,
        sensitiveFields: typing.Union[MetaOapg.properties.sensitiveFields, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        internalOptions: typing.Union[MetaOapg.properties.internalOptions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        onboardSteps: typing.Union[MetaOapg.properties.onboardSteps, list, tuple, schemas.Unset] = schemas.unset,
        onboarding: typing.Union[MetaOapg.properties.onboarding, bool, schemas.Unset] = schemas.unset,
        selfServeImporting: typing.Union[MetaOapg.properties.selfServeImporting, bool, schemas.Unset] = schemas.unset,
        headCount: typing.Union[MetaOapg.properties.headCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userCount: typing.Union[MetaOapg.properties.userCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activeUserCount: typing.Union[MetaOapg.properties.activeUserCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activeAt: typing.Union[MetaOapg.properties.activeAt, str, schemas.Unset] = schemas.unset,
        changeAt: typing.Union[MetaOapg.properties.changeAt, str, schemas.Unset] = schemas.unset,
        createId: typing.Union[MetaOapg.properties.createId, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, schemas.Unset] = schemas.unset,
        destroyAt: typing.Union[MetaOapg.properties.destroyAt, str, schemas.Unset] = schemas.unset,
        destroyId: typing.Union[MetaOapg.properties.destroyId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Org':
        return super().__new__(
            cls,
            *args,
            name=name,
            id=id,
            slug=slug,
            customerId=customerId,
            type=type,
            industry=industry,
            estEmployees=estEmployees,
            estRevenue=estRevenue,
            foundedYear=foundedYear,
            address=address,
            phone=phone,
            email=email,
            url=url,
            domains=domains,
            status=status,
            imagePath=imagePath,
            currencies=currencies,
            stock=stock,
            timezone=timezone,
            appTime=appTime,
            zone=zone,
            fiscalStart=fiscalStart,
            headJobId=headJobId,
            startDate=startDate,
            sensitiveFields=sensitiveFields,
            options=options,
            internalOptions=internalOptions,
            onboardSteps=onboardSteps,
            onboarding=onboarding,
            selfServeImporting=selfServeImporting,
            headCount=headCount,
            userCount=userCount,
            activeUserCount=activeUserCount,
            activeAt=activeAt,
            changeAt=changeAt,
            createId=createId,
            createAt=createAt,
            updateId=updateId,
            updateAt=updateAt,
            destroyAt=destroyAt,
            destroyId=destroyId,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.address import Address
from chart_hop_python_sdk.model.onboard_step_result import OnboardStepResult
from chart_hop_python_sdk.model.org_currencies import OrgCurrencies
from chart_hop_python_sdk.model.org_domain import OrgDomain
