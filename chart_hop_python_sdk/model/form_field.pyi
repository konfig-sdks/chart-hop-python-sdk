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


class FormField(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "longLabel",
            "label",
            "required",
            "fieldId",
        }
        
        class properties:
            fieldId = schemas.StrSchema
            label = schemas.StrSchema
            required = schemas.BoolSchema
            longLabel = schemas.BoolSchema
            __annotations__ = {
                "fieldId": fieldId,
                "label": label,
                "required": required,
                "longLabel": longLabel,
            }
    
    longLabel: MetaOapg.properties.longLabel
    label: MetaOapg.properties.label
    required: MetaOapg.properties.required
    fieldId: MetaOapg.properties.fieldId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldId"]) -> MetaOapg.properties.fieldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longLabel"]) -> MetaOapg.properties.longLabel: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fieldId", "label", "required", "longLabel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldId"]) -> MetaOapg.properties.fieldId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longLabel"]) -> MetaOapg.properties.longLabel: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fieldId", "label", "required", "longLabel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        longLabel: typing.Union[MetaOapg.properties.longLabel, bool, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        fieldId: typing.Union[MetaOapg.properties.fieldId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormField':
        return super().__new__(
            cls,
            *args,
            longLabel=longLabel,
            label=label,
            required=required,
            fieldId=fieldId,
            _configuration=_configuration,
            **kwargs,
        )
