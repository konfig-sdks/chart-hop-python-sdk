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


class CreateQuestion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "question",
        }
        
        class properties:
            question = schemas.StrSchema
            orgId = schemas.StrSchema
            fieldId = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ADDRESS(cls):
                    return cls("ADDRESS")
                
                @schemas.classproperty
                def BOOLEAN(cls):
                    return cls("BOOLEAN")
                
                @schemas.classproperty
                def COMP(cls):
                    return cls("COMP")
                
                @schemas.classproperty
                def COMPOUND(cls):
                    return cls("COMPOUND")
                
                @schemas.classproperty
                def COMP_BAND(cls):
                    return cls("COMP_BAND")
                
                @schemas.classproperty
                def CONTACTS(cls):
                    return cls("CONTACTS")
                
                @schemas.classproperty
                def CURRENCY(cls):
                    return cls("CURRENCY")
                
                @schemas.classproperty
                def DATE(cls):
                    return cls("DATE")
                
                @schemas.classproperty
                def DECIMAL(cls):
                    return cls("DECIMAL")
                
                @schemas.classproperty
                def ELAPSED_DAYS(cls):
                    return cls("ELAPSED_DAYS")
                
                @schemas.classproperty
                def ELAPSED_MONTHS(cls):
                    return cls("ELAPSED_MONTHS")
                
                @schemas.classproperty
                def ELAPSED_YEARS(cls):
                    return cls("ELAPSED_YEARS")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("EMAIL")
                
                @schemas.classproperty
                def ENUM(cls):
                    return cls("ENUM")
                
                @schemas.classproperty
                def ENUM_EXPR(cls):
                    return cls("ENUM_EXPR")
                
                @schemas.classproperty
                def ENUM_MULTI(cls):
                    return cls("ENUM_MULTI")
                
                @schemas.classproperty
                def ENUM_SCALE(cls):
                    return cls("ENUM_SCALE")
                
                @schemas.classproperty
                def EXPR(cls):
                    return cls("EXPR")
                
                @schemas.classproperty
                def FILE(cls):
                    return cls("FILE")
                
                @schemas.classproperty
                def GROUP(cls):
                    return cls("GROUP")
                
                @schemas.classproperty
                def GROUPS(cls):
                    return cls("GROUPS")
                
                @schemas.classproperty
                def GROUP_ASSIGNMENTS(cls):
                    return cls("GROUP_ASSIGNMENTS")
                
                @schemas.classproperty
                def GROUP_TYPE(cls):
                    return cls("GROUP_TYPE")
                
                @schemas.classproperty
                def IMAGE(cls):
                    return cls("IMAGE")
                
                @schemas.classproperty
                def INTEGER(cls):
                    return cls("INTEGER")
                
                @schemas.classproperty
                def JOB(cls):
                    return cls("JOB")
                
                @schemas.classproperty
                def JOBS(cls):
                    return cls("JOBS")
                
                @schemas.classproperty
                def JOB_TIER(cls):
                    return cls("JOB_TIER")
                
                @schemas.classproperty
                def LIST(cls):
                    return cls("LIST")
                
                @schemas.classproperty
                def MONEY(cls):
                    return cls("MONEY")
                
                @schemas.classproperty
                def NAME(cls):
                    return cls("NAME")
                
                @schemas.classproperty
                def OBJECT(cls):
                    return cls("OBJECT")
                
                @schemas.classproperty
                def PAY_INTERVAL(cls):
                    return cls("PAY_INTERVAL")
                
                @schemas.classproperty
                def PERCENT(cls):
                    return cls("PERCENT")
                
                @schemas.classproperty
                def PERSON(cls):
                    return cls("PERSON")
                
                @schemas.classproperty
                def PERSONS(cls):
                    return cls("PERSONS")
                
                @schemas.classproperty
                def PHONE(cls):
                    return cls("PHONE")
                
                @schemas.classproperty
                def STOCKGRANT(cls):
                    return cls("STOCKGRANT")
                
                @schemas.classproperty
                def STRING(cls):
                    return cls("STRING")
                
                @schemas.classproperty
                def TABLE_REF(cls):
                    return cls("TABLE_REF")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("TEXT")
                
                @schemas.classproperty
                def TIMEOFF(cls):
                    return cls("TIMEOFF")
                
                @schemas.classproperty
                def TIMESTAMP(cls):
                    return cls("TIMESTAMP")
                
                @schemas.classproperty
                def TRACKED_GROUP(cls):
                    return cls("TRACKED_GROUP")
                
                @schemas.classproperty
                def URL(cls):
                    return cls("URL")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("USER")
                
                @schemas.classproperty
                def VARIABLE_COMP(cls):
                    return cls("VARIABLE_COMP")
                
                @schemas.classproperty
                def VARIABLE_COMPS(cls):
                    return cls("VARIABLE_COMPS")
            
            
            class plural(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("SINGLE")
                
                @schemas.classproperty
                def LIST(cls):
                    return cls("LIST")
                
                @schemas.classproperty
                def SET(cls):
                    return cls("SET")
            
            
            class values(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EnumValue']:
                        return EnumValue
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EnumValue'], typing.List['EnumValue']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'values':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EnumValue':
                    return super().__getitem__(i)
            options = schemas.DictSchema
            __annotations__ = {
                "question": question,
                "orgId": orgId,
                "fieldId": fieldId,
                "type": type,
                "plural": plural,
                "values": values,
                "options": options,
            }
    
    question: MetaOapg.properties.question
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldId"]) -> MetaOapg.properties.fieldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plural"]) -> MetaOapg.properties.plural: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> MetaOapg.properties.values: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["question", "orgId", "fieldId", "type", "plural", "values", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldId"]) -> typing.Union[MetaOapg.properties.fieldId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plural"]) -> typing.Union[MetaOapg.properties.plural, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union[MetaOapg.properties.values, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["question", "orgId", "fieldId", "type", "plural", "values", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        question: typing.Union[MetaOapg.properties.question, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        fieldId: typing.Union[MetaOapg.properties.fieldId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        plural: typing.Union[MetaOapg.properties.plural, str, schemas.Unset] = schemas.unset,
        values: typing.Union[MetaOapg.properties.values, list, tuple, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateQuestion':
        return super().__new__(
            cls,
            *args,
            question=question,
            orgId=orgId,
            fieldId=fieldId,
            type=type,
            plural=plural,
            values=values,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.enum_value import EnumValue