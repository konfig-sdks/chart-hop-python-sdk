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


class ReportSeriesResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "color",
            "data",
            "format",
            "isIntervalMetric",
            "label",
        }
        
        class properties:
            label = schemas.StrSchema
            color = schemas.StrSchema
            format = schemas.StrSchema
        
            @staticmethod
            def data() -> typing.Type['ReportSeriesResultData']:
                return ReportSeriesResultData
            isIntervalMetric = schemas.BoolSchema
            
            
            class xAxis(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LabelColor']:
                        return LabelColor
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LabelColor'], typing.List['LabelColor']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'xAxis':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LabelColor':
                    return super().__getitem__(i)
            __annotations__ = {
                "label": label,
                "color": color,
                "format": format,
                "data": data,
                "isIntervalMetric": isIntervalMetric,
                "xAxis": xAxis,
            }
    
    color: MetaOapg.properties.color
    data: 'ReportSeriesResultData'
    format: MetaOapg.properties.format
    isIntervalMetric: MetaOapg.properties.isIntervalMetric
    label: MetaOapg.properties.label
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ReportSeriesResultData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isIntervalMetric"]) -> MetaOapg.properties.isIntervalMetric: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["xAxis"]) -> MetaOapg.properties.xAxis: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["label", "color", "format", "data", "isIntervalMetric", "xAxis", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ReportSeriesResultData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isIntervalMetric"]) -> MetaOapg.properties.isIntervalMetric: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["xAxis"]) -> typing.Union[MetaOapg.properties.xAxis, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["label", "color", "format", "data", "isIntervalMetric", "xAxis", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        data: 'ReportSeriesResultData',
        format: typing.Union[MetaOapg.properties.format, str, ],
        isIntervalMetric: typing.Union[MetaOapg.properties.isIntervalMetric, bool, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        xAxis: typing.Union[MetaOapg.properties.xAxis, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportSeriesResult':
        return super().__new__(
            cls,
            *args,
            color=color,
            data=data,
            format=format,
            isIntervalMetric=isIntervalMetric,
            label=label,
            xAxis=xAxis,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.label_color import LabelColor
from chart_hop_python_sdk.model.report_series_result_data import ReportSeriesResultData
