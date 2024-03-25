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


class UpdateReport(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            label = schemas.StrSchema
            filter = schemas.StrSchema
            
            
            class share(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NORMAL": "NORMAL",
                        "FULL": "FULL",
                    }
                
                @schemas.classproperty
                def NORMAL(cls):
                    return cls("NORMAL")
                
                @schemas.classproperty
                def FULL(cls):
                    return cls("FULL")
            
            
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
        
            @staticmethod
            def chartIds() -> typing.Type['UpdateReportChartIds']:
                return UpdateReportChartIds
            __annotations__ = {
                "description": description,
                "label": label,
                "filter": filter,
                "share": share,
                "sensitive": sensitive,
                "shareAccess": shareAccess,
                "chartIds": chartIds,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["share"]) -> MetaOapg.properties.share: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareAccess"]) -> MetaOapg.properties.shareAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chartIds"]) -> 'UpdateReportChartIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "label", "filter", "share", "sensitive", "shareAccess", "chartIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["share"]) -> typing.Union[MetaOapg.properties.share, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitive"]) -> typing.Union[MetaOapg.properties.sensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareAccess"]) -> typing.Union[MetaOapg.properties.shareAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chartIds"]) -> typing.Union['UpdateReportChartIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "label", "filter", "share", "sensitive", "shareAccess", "chartIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, str, schemas.Unset] = schemas.unset,
        share: typing.Union[MetaOapg.properties.share, str, schemas.Unset] = schemas.unset,
        sensitive: typing.Union[MetaOapg.properties.sensitive, str, schemas.Unset] = schemas.unset,
        shareAccess: typing.Union[MetaOapg.properties.shareAccess, list, tuple, schemas.Unset] = schemas.unset,
        chartIds: typing.Union['UpdateReportChartIds', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateReport':
        return super().__new__(
            cls,
            *args,
            description=description,
            label=label,
            filter=filter,
            share=share,
            sensitive=sensitive,
            shareAccess=shareAccess,
            chartIds=chartIds,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.share_access import ShareAccess
from chart_hop_python_sdk.model.update_report_chart_ids import UpdateReportChartIds
