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


class ReportDateInterval(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "endDate",
            "startDate",
        }
        
        class properties:
            startDate = schemas.DateSchema
            endDate = schemas.DateSchema
            partialStartDate = schemas.DateSchema
            partialEndDate = schemas.DateSchema
            __annotations__ = {
                "startDate": startDate,
                "endDate": endDate,
                "partialStartDate": partialStartDate,
                "partialEndDate": partialEndDate,
            }
    
    endDate: MetaOapg.properties.endDate
    startDate: MetaOapg.properties.startDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partialStartDate"]) -> MetaOapg.properties.partialStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partialEndDate"]) -> MetaOapg.properties.partialEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["startDate", "endDate", "partialStartDate", "partialEndDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partialStartDate"]) -> typing.Union[MetaOapg.properties.partialStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partialEndDate"]) -> typing.Union[MetaOapg.properties.partialEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["startDate", "endDate", "partialStartDate", "partialEndDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, ],
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, ],
        partialStartDate: typing.Union[MetaOapg.properties.partialStartDate, str, date, schemas.Unset] = schemas.unset,
        partialEndDate: typing.Union[MetaOapg.properties.partialEndDate, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportDateInterval':
        return super().__new__(
            cls,
            *args,
            endDate=endDate,
            startDate=startDate,
            partialStartDate=partialStartDate,
            partialEndDate=partialEndDate,
            _configuration=_configuration,
            **kwargs,
        )
