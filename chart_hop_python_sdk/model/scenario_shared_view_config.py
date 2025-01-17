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


class ScenarioSharedViewConfig(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def customColumnNames() -> typing.Type['ScenarioSharedViewConfigCustomColumnNames']:
                return ScenarioSharedViewConfigCustomColumnNames
        
            @staticmethod
            def columnWidths() -> typing.Type['ScenarioSharedViewConfigColumnWidths']:
                return ScenarioSharedViewConfigColumnWidths
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ALL_CHANGES_GROUPED": "ALL_CHANGES_GROUPED",
                    }
                
                @schemas.classproperty
                def ALL_CHANGES_GROUPED(cls):
                    return cls("ALL_CHANGES_GROUPED")
            updateId = schemas.StrSchema
            updateAt = schemas.Int64Schema
            __annotations__ = {
                "customColumnNames": customColumnNames,
                "columnWidths": columnWidths,
                "type": type,
                "updateId": updateId,
                "updateAt": updateAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customColumnNames"]) -> 'ScenarioSharedViewConfigCustomColumnNames': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columnWidths"]) -> 'ScenarioSharedViewConfigColumnWidths': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateId"]) -> MetaOapg.properties.updateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateAt"]) -> MetaOapg.properties.updateAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customColumnNames", "columnWidths", "type", "updateId", "updateAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customColumnNames"]) -> typing.Union['ScenarioSharedViewConfigCustomColumnNames', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columnWidths"]) -> typing.Union['ScenarioSharedViewConfigColumnWidths', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateId"]) -> typing.Union[MetaOapg.properties.updateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateAt"]) -> typing.Union[MetaOapg.properties.updateAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customColumnNames", "columnWidths", "type", "updateId", "updateAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customColumnNames: typing.Union['ScenarioSharedViewConfigCustomColumnNames', schemas.Unset] = schemas.unset,
        columnWidths: typing.Union['ScenarioSharedViewConfigColumnWidths', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        updateId: typing.Union[MetaOapg.properties.updateId, str, schemas.Unset] = schemas.unset,
        updateAt: typing.Union[MetaOapg.properties.updateAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScenarioSharedViewConfig':
        return super().__new__(
            cls,
            *args,
            customColumnNames=customColumnNames,
            columnWidths=columnWidths,
            type=type,
            updateId=updateId,
            updateAt=updateAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.scenario_shared_view_config_column_widths import ScenarioSharedViewConfigColumnWidths
from chart_hop_python_sdk.model.scenario_shared_view_config_custom_column_names import ScenarioSharedViewConfigCustomColumnNames
