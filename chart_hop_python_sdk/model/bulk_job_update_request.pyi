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


class BulkJobUpdateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "updates",
        }
        
        class properties:
            
            
            class updates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UpdateOperation']:
                        return UpdateOperation
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UpdateOperation'], typing.List['UpdateOperation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'updates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UpdateOperation':
                    return super().__getitem__(i)
            date = schemas.DateSchema
            scenarioId = schemas.StrSchema
            note = schemas.StrSchema
            __annotations__ = {
                "updates": updates,
                "date": date,
                "scenarioId": scenarioId,
                "note": note,
            }
    
    date: MetaOapg.properties.date
    updates: MetaOapg.properties.updates
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updates"]) -> MetaOapg.properties.updates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenarioId"]) -> MetaOapg.properties.scenarioId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["updates", "date", "scenarioId", "note", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updates"]) -> MetaOapg.properties.updates: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenarioId"]) -> typing.Union[MetaOapg.properties.scenarioId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["updates", "date", "scenarioId", "note", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, date, ],
        updates: typing.Union[MetaOapg.properties.updates, list, tuple, ],
        scenarioId: typing.Union[MetaOapg.properties.scenarioId, str, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkJobUpdateRequest':
        return super().__new__(
            cls,
            *args,
            date=date,
            updates=updates,
            scenarioId=scenarioId,
            note=note,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.update_operation import UpdateOperation
