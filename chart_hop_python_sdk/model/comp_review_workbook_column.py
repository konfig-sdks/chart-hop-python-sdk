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


class CompReviewWorkbookColumn(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "visibleToGroups",
            "name",
            "visibleToType",
            "editableFor",
            "visibleTo",
            "label",
        }
        
        class properties:
            name = schemas.StrSchema
            label = schemas.StrSchema
            editableFor = schemas.StrSchema
            visibleTo = schemas.StrSchema
        
            @staticmethod
            def visibleToGroups() -> typing.Type['CompReviewWorkbookColumnVisibleToGroups']:
                return CompReviewWorkbookColumnVisibleToGroups
            
            
            class visibleToType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EVERYONE": "EVERYONE",
                        "DEPARTMENT": "DEPARTMENT",
                        "TEAM": "TEAM",
                        "LOCATION": "LOCATION",
                        "CUSTOM": "CUSTOM",
                    }
                
                @schemas.classproperty
                def EVERYONE(cls):
                    return cls("EVERYONE")
                
                @schemas.classproperty
                def DEPARTMENT(cls):
                    return cls("DEPARTMENT")
                
                @schemas.classproperty
                def TEAM(cls):
                    return cls("TEAM")
                
                @schemas.classproperty
                def LOCATION(cls):
                    return cls("LOCATION")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("CUSTOM")
            color = schemas.StrSchema
        
            @staticmethod
            def visibleToRoles() -> typing.Type['InCycleViewFeatures']:
                return InCycleViewFeatures
            __annotations__ = {
                "name": name,
                "label": label,
                "editableFor": editableFor,
                "visibleTo": visibleTo,
                "visibleToGroups": visibleToGroups,
                "visibleToType": visibleToType,
                "color": color,
                "visibleToRoles": visibleToRoles,
            }
    
    visibleToGroups: 'CompReviewWorkbookColumnVisibleToGroups'
    name: MetaOapg.properties.name
    visibleToType: MetaOapg.properties.visibleToType
    editableFor: MetaOapg.properties.editableFor
    visibleTo: MetaOapg.properties.visibleTo
    label: MetaOapg.properties.label
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editableFor"]) -> MetaOapg.properties.editableFor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibleTo"]) -> MetaOapg.properties.visibleTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibleToGroups"]) -> 'CompReviewWorkbookColumnVisibleToGroups': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibleToType"]) -> MetaOapg.properties.visibleToType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibleToRoles"]) -> 'InCycleViewFeatures': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "label", "editableFor", "visibleTo", "visibleToGroups", "visibleToType", "color", "visibleToRoles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editableFor"]) -> MetaOapg.properties.editableFor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibleTo"]) -> MetaOapg.properties.visibleTo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibleToGroups"]) -> 'CompReviewWorkbookColumnVisibleToGroups': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibleToType"]) -> MetaOapg.properties.visibleToType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibleToRoles"]) -> typing.Union['InCycleViewFeatures', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "label", "editableFor", "visibleTo", "visibleToGroups", "visibleToType", "color", "visibleToRoles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        visibleToGroups: 'CompReviewWorkbookColumnVisibleToGroups',
        name: typing.Union[MetaOapg.properties.name, str, ],
        visibleToType: typing.Union[MetaOapg.properties.visibleToType, str, ],
        editableFor: typing.Union[MetaOapg.properties.editableFor, str, ],
        visibleTo: typing.Union[MetaOapg.properties.visibleTo, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        visibleToRoles: typing.Union['InCycleViewFeatures', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompReviewWorkbookColumn':
        return super().__new__(
            cls,
            *args,
            visibleToGroups=visibleToGroups,
            name=name,
            visibleToType=visibleToType,
            editableFor=editableFor,
            visibleTo=visibleTo,
            label=label,
            color=color,
            visibleToRoles=visibleToRoles,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.comp_review_workbook_column_visible_to_groups import CompReviewWorkbookColumnVisibleToGroups
from chart_hop_python_sdk.model.in_cycle_view_features import InCycleViewFeatures
