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


class UpdateScenario(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            name = schemas.StrSchema
            startDate = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "OPEN": "OPEN",
                        "INACTIVE": "INACTIVE",
                        "MERGED": "MERGED",
                        "DRAFT": "DRAFT",
                        "ARCHIVED": "ARCHIVED",
                    }
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("OPEN")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def MERGED(cls):
                    return cls("MERGED")
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("DRAFT")
                
                @schemas.classproperty
                def ARCHIVED(cls):
                    return cls("ARCHIVED")
            
            
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
            
            
            class startDateFixed(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "FIXED": "FIXED",
                        "TODAY": "TODAY",
                    }
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("FIXED")
                
                @schemas.classproperty
                def TODAY(cls):
                    return cls("TODAY")
        
            @staticmethod
            def validJobIdSet() -> typing.Type['UpdateScenarioValidJobIdSet']:
                return UpdateScenarioValidJobIdSet
            entityId = schemas.StrSchema
            
            
            class entityType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMP_REVIEW": "COMP_REVIEW",
                    }
                
                @schemas.classproperty
                def COMP_REVIEW(cls):
                    return cls("COMP_REVIEW")
            
            
            class sharedViewConfig(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['ScenarioSharedViewConfig']:
                        return ScenarioSharedViewConfig
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ScenarioSharedViewConfig'], typing.List['ScenarioSharedViewConfig']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sharedViewConfig':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ScenarioSharedViewConfig':
                    return super().__getitem__(i)
        
            @staticmethod
            def budget() -> typing.Type['Money']:
                return Money
            costCalc = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "name": name,
                "startDate": startDate,
                "status": status,
                "shareAccess": shareAccess,
                "startDateFixed": startDateFixed,
                "validJobIdSet": validJobIdSet,
                "entityId": entityId,
                "entityType": entityType,
                "sharedViewConfig": sharedViewConfig,
                "budget": budget,
                "costCalc": costCalc,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDateFixed"]) -> MetaOapg.properties.startDateFixed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validJobIdSet"]) -> 'UpdateScenarioValidJobIdSet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityType"]) -> MetaOapg.properties.entityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sharedViewConfig"]) -> MetaOapg.properties.sharedViewConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budget"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCalc"]) -> MetaOapg.properties.costCalc: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "startDate", "status", "shareAccess", "startDateFixed", "validJobIdSet", "entityId", "entityType", "sharedViewConfig", "budget", "costCalc", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDateFixed"]) -> typing.Union[MetaOapg.properties.startDateFixed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validJobIdSet"]) -> typing.Union['UpdateScenarioValidJobIdSet', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityId"]) -> typing.Union[MetaOapg.properties.entityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityType"]) -> typing.Union[MetaOapg.properties.entityType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sharedViewConfig"]) -> typing.Union[MetaOapg.properties.sharedViewConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budget"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCalc"]) -> typing.Union[MetaOapg.properties.costCalc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "startDate", "status", "shareAccess", "startDateFixed", "validJobIdSet", "entityId", "entityType", "sharedViewConfig", "budget", "costCalc", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        startDateFixed: typing.Union[MetaOapg.properties.startDateFixed, str, schemas.Unset] = schemas.unset,
        validJobIdSet: typing.Union['UpdateScenarioValidJobIdSet', schemas.Unset] = schemas.unset,
        entityId: typing.Union[MetaOapg.properties.entityId, str, schemas.Unset] = schemas.unset,
        entityType: typing.Union[MetaOapg.properties.entityType, str, schemas.Unset] = schemas.unset,
        sharedViewConfig: typing.Union[MetaOapg.properties.sharedViewConfig, list, tuple, schemas.Unset] = schemas.unset,
        budget: typing.Union['Money', schemas.Unset] = schemas.unset,
        costCalc: typing.Union[MetaOapg.properties.costCalc, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateScenario':
        return super().__new__(
            cls,
            *args,
            description=description,
            name=name,
            startDate=startDate,
            status=status,
            shareAccess=shareAccess,
            startDateFixed=startDateFixed,
            validJobIdSet=validJobIdSet,
            entityId=entityId,
            entityType=entityType,
            sharedViewConfig=sharedViewConfig,
            budget=budget,
            costCalc=costCalc,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.money import Money
from chart_hop_python_sdk.model.scenario_shared_view_config import ScenarioSharedViewConfig
from chart_hop_python_sdk.model.share_access import ShareAccess
from chart_hop_python_sdk.model.update_scenario_valid_job_id_set import UpdateScenarioValidJobIdSet
