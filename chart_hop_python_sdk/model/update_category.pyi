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


class UpdateCategory(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            label = schemas.StrSchema
        
            @staticmethod
            def fieldIds() -> typing.Type['UpdateCategoryFieldIds']:
                return UpdateCategoryFieldIds
        
            @staticmethod
            def nativeFields() -> typing.Type['UpdateCategoryNativeFields']:
                return UpdateCategoryNativeFields
            __annotations__ = {
                "label": label,
                "fieldIds": fieldIds,
                "nativeFields": nativeFields,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldIds"]) -> 'UpdateCategoryFieldIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nativeFields"]) -> 'UpdateCategoryNativeFields': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["label", "fieldIds", "nativeFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldIds"]) -> typing.Union['UpdateCategoryFieldIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nativeFields"]) -> typing.Union['UpdateCategoryNativeFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["label", "fieldIds", "nativeFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        fieldIds: typing.Union['UpdateCategoryFieldIds', schemas.Unset] = schemas.unset,
        nativeFields: typing.Union['UpdateCategoryNativeFields', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateCategory':
        return super().__new__(
            cls,
            *args,
            label=label,
            fieldIds=fieldIds,
            nativeFields=nativeFields,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.update_category_field_ids import UpdateCategoryFieldIds
from chart_hop_python_sdk.model.update_category_native_fields import UpdateCategoryNativeFields
