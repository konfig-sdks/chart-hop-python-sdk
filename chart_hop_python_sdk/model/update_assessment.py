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


class UpdateAssessment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            label = schemas.StrSchema
            slug = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "REVIEW": "REVIEW",
                        "COMP_REVIEW": "COMP_REVIEW",
                        "SURVEY": "SURVEY",
                    }
                
                @schemas.classproperty
                def REVIEW(cls):
                    return cls("REVIEW")
                
                @schemas.classproperty
                def COMP_REVIEW(cls):
                    return cls("COMP_REVIEW")
                
                @schemas.classproperty
                def SURVEY(cls):
                    return cls("SURVEY")
            fields = schemas.DictSchema
            
            
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
            
            
            class sensitive(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "GLOBAL": "GLOBAL",
                        "ORG": "ORG",
                        "ORG_OTHER": "ORG_OTHER",
                        "PERSONAL_DEMOG": "PERSONAL_DEMOG",
                        "PERSONAL_BIRTH": "PERSONAL_BIRTH",
                        "PERSONAL_CONTACT": "PERSONAL_CONTACT",
                        "PERSONAL_PRIVATE": "PERSONAL_PRIVATE",
                        "SENSITIVE_BIRTH": "SENSITIVE_BIRTH",
                        "SENSITIVE_CONTACT": "SENSITIVE_CONTACT",
                        "TIMEOFF": "TIMEOFF",
                        "COMP_CASH": "COMP_CASH",
                        "COMP_EQUITY": "COMP_EQUITY",
                        "SENSITIVE": "SENSITIVE",
                        "PERSONAL": "PERSONAL",
                        "MANAGER": "MANAGER",
                        "GRAND_MANAGER": "GRAND_MANAGER",
                        "DIRECT": "DIRECT",
                        "PEERS": "PEERS",
                        "HIGH": "HIGH",
                        "PRIVATE": "PRIVATE",
                    }
                
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
            
            
            class color(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^#[a-f0-9]{6}$',
                    }]
            startDate = schemas.DateSchema
            endDate = schemas.DateSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DRAFT": "DRAFT",
                        "ACTIVE": "ACTIVE",
                        "DONE": "DONE",
                    }
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("DRAFT")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("DONE")
            doneAt = schemas.StrSchema
            taskCount = schemas.Int32Schema
            taskDoneCount = schemas.Int32Schema
            peopleIncludedCount = schemas.Int32Schema
            query = schemas.StrSchema
            __annotations__ = {
                "label": label,
                "slug": slug,
                "type": type,
                "fields": fields,
                "shareAccess": shareAccess,
                "sensitive": sensitive,
                "color": color,
                "startDate": startDate,
                "endDate": endDate,
                "status": status,
                "doneAt": doneAt,
                "taskCount": taskCount,
                "taskDoneCount": taskDoneCount,
                "peopleIncludedCount": peopleIncludedCount,
                "query": query,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doneAt"]) -> MetaOapg.properties.doneAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskCount"]) -> MetaOapg.properties.taskCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskDoneCount"]) -> MetaOapg.properties.taskDoneCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["peopleIncludedCount"]) -> MetaOapg.properties.peopleIncludedCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["label", "slug", "type", "fields", "shareAccess", "sensitive", "color", "startDate", "endDate", "status", "doneAt", "taskCount", "taskDoneCount", "peopleIncludedCount", "query", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union[MetaOapg.properties.fields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitive"]) -> typing.Union[MetaOapg.properties.sensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doneAt"]) -> typing.Union[MetaOapg.properties.doneAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskCount"]) -> typing.Union[MetaOapg.properties.taskCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskDoneCount"]) -> typing.Union[MetaOapg.properties.taskDoneCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["peopleIncludedCount"]) -> typing.Union[MetaOapg.properties.peopleIncludedCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["label", "slug", "type", "fields", "shareAccess", "sensitive", "color", "startDate", "endDate", "status", "doneAt", "taskCount", "taskDoneCount", "peopleIncludedCount", "query", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        fields: typing.Union[MetaOapg.properties.fields, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        sensitive: typing.Union[MetaOapg.properties.sensitive, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        doneAt: typing.Union[MetaOapg.properties.doneAt, str, schemas.Unset] = schemas.unset,
        taskCount: typing.Union[MetaOapg.properties.taskCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taskDoneCount: typing.Union[MetaOapg.properties.taskDoneCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        peopleIncludedCount: typing.Union[MetaOapg.properties.peopleIncludedCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateAssessment':
        return super().__new__(
            cls,
            *args,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            shareAccess=shareAccess,
            sensitive=sensitive,
            color=color,
            startDate=startDate,
            endDate=endDate,
            status=status,
            doneAt=doneAt,
            taskCount=taskCount,
            taskDoneCount=taskDoneCount,
            peopleIncludedCount=peopleIncludedCount,
            query=query,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.share_access import ShareAccess