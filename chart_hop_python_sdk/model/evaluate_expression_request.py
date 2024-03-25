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


class EvaluateExpressionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entityType",
            "entityId",
            "expr",
        }
        
        class properties:
            expr = schemas.StrSchema
            
            
            class entityType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTION": "ACTION",
                        "AGREEMENT": "AGREEMENT",
                        "APP": "APP",
                        "APP_CONFIG": "APP_CONFIG",
                        "APPROVAL_CHAIN": "APPROVAL_CHAIN",
                        "APPROVAL_CHAIN_STAGE": "APPROVAL_CHAIN_STAGE",
                        "APPROVAL_REQUEST": "APPROVAL_REQUEST",
                        "ASSESSMENT": "ASSESSMENT",
                        "BUDGET_POOL": "BUDGET_POOL",
                        "BUNDLE": "BUNDLE",
                        "CATEGORY": "CATEGORY",
                        "CATEGORY_SORT": "CATEGORY_SORT",
                        "CHANGE": "CHANGE",
                        "COMMENT": "COMMENT",
                        "COMP_BAND": "COMP_BAND",
                        "COMP_REVIEW": "COMP_REVIEW",
                        "CONTENT": "CONTENT",
                        "CUSTOMER": "CUSTOMER",
                        "DATA_VIEW": "DATA_VIEW",
                        "EXCHANGE_RATE": "EXCHANGE_RATE",
                        "EMAIL_TEMPLATE": "EMAIL_TEMPLATE",
                        "FIELD": "FIELD",
                        "FILE": "FILE",
                        "FORM": "FORM",
                        "FORM_DRAFT": "FORM_DRAFT",
                        "FORM_RESPONSE": "FORM_RESPONSE",
                        "GEOCODE": "GEOCODE",
                        "GROUP": "GROUP",
                        "GUIDELINE": "GUIDELINE",
                        "JOB": "JOB",
                        "JOB_LEVEL": "JOB_LEVEL",
                        "MEDIA": "MEDIA",
                        "MESSAGE": "MESSAGE",
                        "MULTIPLIER": "MULTIPLIER",
                        "ORG": "ORG",
                        "ORG_CONFIG": "ORG_CONFIG",
                        "PERSON": "PERSON",
                        "PROFILE_TAB": "PROFILE_TAB",
                        "POLICY": "POLICY",
                        "POSITION": "POSITION",
                        "PROCESS": "PROCESS",
                        "PRODUCT": "PRODUCT",
                        "QUERY_TOKEN": "QUERY_TOKEN",
                        "QUESTION": "QUESTION",
                        "REPORT": "REPORT",
                        "REPORT_CHART": "REPORT_CHART",
                        "ROLE": "ROLE",
                        "SCENARIO": "SCENARIO",
                        "STOCK_PRICE": "STOCK_PRICE",
                        "TABLE": "TABLE",
                        "TABLE_ROW": "TABLE_ROW",
                        "TASK_CONFIG": "TASK_CONFIG",
                        "TEMPLATE": "TEMPLATE",
                        "TASK": "TASK",
                        "TOKEN": "TOKEN",
                        "TIMEOFF": "TIMEOFF",
                        "TRACKED_GROUP": "TRACKED_GROUP",
                        "USER": "USER",
                    }
                
                @schemas.classproperty
                def ACTION(cls):
                    return cls("ACTION")
                
                @schemas.classproperty
                def AGREEMENT(cls):
                    return cls("AGREEMENT")
                
                @schemas.classproperty
                def APP(cls):
                    return cls("APP")
                
                @schemas.classproperty
                def APP_CONFIG(cls):
                    return cls("APP_CONFIG")
                
                @schemas.classproperty
                def APPROVAL_CHAIN(cls):
                    return cls("APPROVAL_CHAIN")
                
                @schemas.classproperty
                def APPROVAL_CHAIN_STAGE(cls):
                    return cls("APPROVAL_CHAIN_STAGE")
                
                @schemas.classproperty
                def APPROVAL_REQUEST(cls):
                    return cls("APPROVAL_REQUEST")
                
                @schemas.classproperty
                def ASSESSMENT(cls):
                    return cls("ASSESSMENT")
                
                @schemas.classproperty
                def BUDGET_POOL(cls):
                    return cls("BUDGET_POOL")
                
                @schemas.classproperty
                def BUNDLE(cls):
                    return cls("BUNDLE")
                
                @schemas.classproperty
                def CATEGORY(cls):
                    return cls("CATEGORY")
                
                @schemas.classproperty
                def CATEGORY_SORT(cls):
                    return cls("CATEGORY_SORT")
                
                @schemas.classproperty
                def CHANGE(cls):
                    return cls("CHANGE")
                
                @schemas.classproperty
                def COMMENT(cls):
                    return cls("COMMENT")
                
                @schemas.classproperty
                def COMP_BAND(cls):
                    return cls("COMP_BAND")
                
                @schemas.classproperty
                def COMP_REVIEW(cls):
                    return cls("COMP_REVIEW")
                
                @schemas.classproperty
                def CONTENT(cls):
                    return cls("CONTENT")
                
                @schemas.classproperty
                def CUSTOMER(cls):
                    return cls("CUSTOMER")
                
                @schemas.classproperty
                def DATA_VIEW(cls):
                    return cls("DATA_VIEW")
                
                @schemas.classproperty
                def EXCHANGE_RATE(cls):
                    return cls("EXCHANGE_RATE")
                
                @schemas.classproperty
                def EMAIL_TEMPLATE(cls):
                    return cls("EMAIL_TEMPLATE")
                
                @schemas.classproperty
                def FIELD(cls):
                    return cls("FIELD")
                
                @schemas.classproperty
                def FILE(cls):
                    return cls("FILE")
                
                @schemas.classproperty
                def FORM(cls):
                    return cls("FORM")
                
                @schemas.classproperty
                def FORM_DRAFT(cls):
                    return cls("FORM_DRAFT")
                
                @schemas.classproperty
                def FORM_RESPONSE(cls):
                    return cls("FORM_RESPONSE")
                
                @schemas.classproperty
                def GEOCODE(cls):
                    return cls("GEOCODE")
                
                @schemas.classproperty
                def GROUP(cls):
                    return cls("GROUP")
                
                @schemas.classproperty
                def GUIDELINE(cls):
                    return cls("GUIDELINE")
                
                @schemas.classproperty
                def JOB(cls):
                    return cls("JOB")
                
                @schemas.classproperty
                def JOB_LEVEL(cls):
                    return cls("JOB_LEVEL")
                
                @schemas.classproperty
                def MEDIA(cls):
                    return cls("MEDIA")
                
                @schemas.classproperty
                def MESSAGE(cls):
                    return cls("MESSAGE")
                
                @schemas.classproperty
                def MULTIPLIER(cls):
                    return cls("MULTIPLIER")
                
                @schemas.classproperty
                def ORG(cls):
                    return cls("ORG")
                
                @schemas.classproperty
                def ORG_CONFIG(cls):
                    return cls("ORG_CONFIG")
                
                @schemas.classproperty
                def PERSON(cls):
                    return cls("PERSON")
                
                @schemas.classproperty
                def PROFILE_TAB(cls):
                    return cls("PROFILE_TAB")
                
                @schemas.classproperty
                def POLICY(cls):
                    return cls("POLICY")
                
                @schemas.classproperty
                def POSITION(cls):
                    return cls("POSITION")
                
                @schemas.classproperty
                def PROCESS(cls):
                    return cls("PROCESS")
                
                @schemas.classproperty
                def PRODUCT(cls):
                    return cls("PRODUCT")
                
                @schemas.classproperty
                def QUERY_TOKEN(cls):
                    return cls("QUERY_TOKEN")
                
                @schemas.classproperty
                def QUESTION(cls):
                    return cls("QUESTION")
                
                @schemas.classproperty
                def REPORT(cls):
                    return cls("REPORT")
                
                @schemas.classproperty
                def REPORT_CHART(cls):
                    return cls("REPORT_CHART")
                
                @schemas.classproperty
                def ROLE(cls):
                    return cls("ROLE")
                
                @schemas.classproperty
                def SCENARIO(cls):
                    return cls("SCENARIO")
                
                @schemas.classproperty
                def STOCK_PRICE(cls):
                    return cls("STOCK_PRICE")
                
                @schemas.classproperty
                def TABLE(cls):
                    return cls("TABLE")
                
                @schemas.classproperty
                def TABLE_ROW(cls):
                    return cls("TABLE_ROW")
                
                @schemas.classproperty
                def TASK_CONFIG(cls):
                    return cls("TASK_CONFIG")
                
                @schemas.classproperty
                def TEMPLATE(cls):
                    return cls("TEMPLATE")
                
                @schemas.classproperty
                def TASK(cls):
                    return cls("TASK")
                
                @schemas.classproperty
                def TOKEN(cls):
                    return cls("TOKEN")
                
                @schemas.classproperty
                def TIMEOFF(cls):
                    return cls("TIMEOFF")
                
                @schemas.classproperty
                def TRACKED_GROUP(cls):
                    return cls("TRACKED_GROUP")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("USER")
            entityId = schemas.StrSchema
            __annotations__ = {
                "expr": expr,
                "entityType": entityType,
                "entityId": entityId,
            }
    
    entityType: MetaOapg.properties.entityType
    entityId: MetaOapg.properties.entityId
    expr: MetaOapg.properties.expr
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expr"]) -> MetaOapg.properties.expr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityType"]) -> MetaOapg.properties.entityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expr", "entityType", "entityId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expr"]) -> MetaOapg.properties.expr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityType"]) -> MetaOapg.properties.entityType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expr", "entityType", "entityId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entityType: typing.Union[MetaOapg.properties.entityType, str, ],
        entityId: typing.Union[MetaOapg.properties.entityId, str, ],
        expr: typing.Union[MetaOapg.properties.expr, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EvaluateExpressionRequest':
        return super().__new__(
            cls,
            *args,
            entityType=entityType,
            entityId=entityId,
            expr=expr,
            _configuration=_configuration,
            **kwargs,
        )