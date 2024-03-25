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


class ReportMetricCollectionItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "persons",
            "jobs",
            "changes",
        }
        
        class properties:
        
            @staticmethod
            def changes() -> typing.Type['ReportMetricCollectionItemChanges']:
                return ReportMetricCollectionItemChanges
        
            @staticmethod
            def jobs() -> typing.Type['ReportMetricCollectionItemJobs']:
                return ReportMetricCollectionItemJobs
        
            @staticmethod
            def persons() -> typing.Type['ReportMetricCollectionItemPersons']:
                return ReportMetricCollectionItemPersons
            __annotations__ = {
                "changes": changes,
                "jobs": jobs,
                "persons": persons,
            }
    
    persons: 'ReportMetricCollectionItemPersons'
    jobs: 'ReportMetricCollectionItemJobs'
    changes: 'ReportMetricCollectionItemChanges'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changes"]) -> 'ReportMetricCollectionItemChanges': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobs"]) -> 'ReportMetricCollectionItemJobs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persons"]) -> 'ReportMetricCollectionItemPersons': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["changes", "jobs", "persons", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changes"]) -> 'ReportMetricCollectionItemChanges': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobs"]) -> 'ReportMetricCollectionItemJobs': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persons"]) -> 'ReportMetricCollectionItemPersons': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["changes", "jobs", "persons", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        persons: 'ReportMetricCollectionItemPersons',
        jobs: 'ReportMetricCollectionItemJobs',
        changes: 'ReportMetricCollectionItemChanges',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportMetricCollectionItem':
        return super().__new__(
            cls,
            *args,
            persons=persons,
            jobs=jobs,
            changes=changes,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.report_metric_collection_item_changes import ReportMetricCollectionItemChanges
from chart_hop_python_sdk.model.report_metric_collection_item_jobs import ReportMetricCollectionItemJobs
from chart_hop_python_sdk.model.report_metric_collection_item_persons import ReportMetricCollectionItemPersons
