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


class ReportChart(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "updateId",
            "createId",
            "query",
            "updateAt",
            "id",
            "label",
            "createAt",
            "orgId",
        }
        
        class properties:
            id = schemas.StrSchema
            orgId = schemas.StrSchema
            label = schemas.StrSchema
        
            @staticmethod
            def query() -> typing.Type['ReportQuery']:
                return ReportQuery
            createId = schemas.StrSchema
            createAt = schemas.StrSchema
            updateId = schemas.StrSchema
            updateAt = schemas.StrSchema
            reportId = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LINE(cls):
                    return cls("LINE")
                
                @schemas.classproperty
                def AREA(cls):
                    return cls("AREA")
                
                @schemas.classproperty
                def STACKED(cls):
                    return cls("STACKED")
                
                @schemas.classproperty
                def BAR(cls):
                    return cls("BAR")
                
                @schemas.classproperty
                def VERTICAL_BAR(cls):
                    return cls("VERTICAL_BAR")
                
                @schemas.classproperty
                def HORIZONTAL_BAR(cls):
                    return cls("HORIZONTAL_BAR")
                
                @schemas.classproperty
                def PIE(cls):
                    return cls("PIE")
                
                @schemas.classproperty
                def TABLE(cls):
                    return cls("TABLE")
                
                @schemas.classproperty
                def TABLE_CROSSTAB(cls):
                    return cls("TABLE_CROSSTAB")
                
                @schemas.classproperty
                def SINGLE_METRIC(cls):
                    return cls("SINGLE_METRIC")
                
                @schemas.classproperty
                def HEADER(cls):
                    return cls("HEADER")
                
                @schemas.classproperty
                def TEXT(cls):
                    return cls("TEXT")
            filter = schemas.StrSchema
            filterOverride = schemas.BoolSchema
            sort = schemas.Int32Schema
            isAdvancedQueryMode = schemas.BoolSchema
            deleteId = schemas.StrSchema
            deleteAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "orgId": orgId,
                "label": label,
                "query": query,
                "createId": createId,
                "createAt": createAt,
                "updateId": updateId,
                "updateAt": updateAt,
                "reportId": reportId,
                "type": type,
                "filter": filter,
                "filterOverride": filterOverride,
                "sort": sort,
                "isAdvancedQueryMode": isAdvancedQueryMode,
                "deleteId": deleteId,
                "deleteAt": deleteAt,
            }
    
    updateId: MetaOapg.properties.updateId
    createId: MetaOapg.properties.createId
    query: 'ReportQuery'
    updateAt: MetaOapg.properties.updateAt
    id: MetaOapg.properties.id
    label: MetaOapg.properties.label
    createAt: MetaOapg.properties.createAt
    orgId: MetaOapg.properties.orgId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> 'ReportQuery': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportId"]) -> MetaOapg.properties.reportId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filterOverride"]) -> MetaOapg.properties.filterOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAdvancedQueryMode"]) -> MetaOapg.properties.isAdvancedQueryMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteId"]) -> MetaOapg.properties.deleteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteAt"]) -> MetaOapg.properties.deleteAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "label", "query", "createId", "createAt", "updateId", "updateAt", "reportId", "type", "filter", "filterOverride", "sort", "isAdvancedQueryMode", "deleteId", "deleteAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> 'ReportQuery': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createId"]) -> MetaOapg.properties.createId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportId"]) -> typing.Union[MetaOapg.properties.reportId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filterOverride"]) -> typing.Union[MetaOapg.properties.filterOverride, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union[MetaOapg.properties.sort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAdvancedQueryMode"]) -> typing.Union[MetaOapg.properties.isAdvancedQueryMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteId"]) -> typing.Union[MetaOapg.properties.deleteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteAt"]) -> typing.Union[MetaOapg.properties.deleteAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "orgId", "label", "query", "createId", "createAt", "updateId", "updateAt", "reportId", "type", "filter", "filterOverride", "sort", "isAdvancedQueryMode", "deleteId", "deleteAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updateId: typing.Union[MetaOapg.properties.updateId, str, ],
        createId: typing.Union[MetaOapg.properties.createId, str, ],
        query: 'ReportQuery',
        updateAt: typing.Union[MetaOapg.properties.updateAt, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        createAt: typing.Union[MetaOapg.properties.createAt, str, ],
        orgId: typing.Union[MetaOapg.properties.orgId, str, ],
        reportId: typing.Union[MetaOapg.properties.reportId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, str, schemas.Unset] = schemas.unset,
        filterOverride: typing.Union[MetaOapg.properties.filterOverride, bool, schemas.Unset] = schemas.unset,
        sort: typing.Union[MetaOapg.properties.sort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isAdvancedQueryMode: typing.Union[MetaOapg.properties.isAdvancedQueryMode, bool, schemas.Unset] = schemas.unset,
        deleteId: typing.Union[MetaOapg.properties.deleteId, str, schemas.Unset] = schemas.unset,
        deleteAt: typing.Union[MetaOapg.properties.deleteAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportChart':
        return super().__new__(
            cls,
            *args,
            updateId=updateId,
            createId=createId,
            query=query,
            updateAt=updateAt,
            id=id,
            label=label,
            createAt=createAt,
            orgId=orgId,
            reportId=reportId,
            type=type,
            filter=filter,
            filterOverride=filterOverride,
            sort=sort,
            isAdvancedQueryMode=isAdvancedQueryMode,
            deleteId=deleteId,
            deleteAt=deleteAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.report_query import ReportQuery
