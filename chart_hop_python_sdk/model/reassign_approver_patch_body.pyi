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


class ReassignApproverPatchBody(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "initialJobId",
            "message",
            "stageOrder",
            "reassignJobId",
        }
        
        class properties:
            stageOrder = schemas.Int32Schema
            initialJobId = schemas.StrSchema
            reassignJobId = schemas.StrSchema
            message = schemas.StrSchema
            __annotations__ = {
                "stageOrder": stageOrder,
                "initialJobId": initialJobId,
                "reassignJobId": reassignJobId,
                "message": message,
            }
    
    initialJobId: MetaOapg.properties.initialJobId
    message: MetaOapg.properties.message
    stageOrder: MetaOapg.properties.stageOrder
    reassignJobId: MetaOapg.properties.reassignJobId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stageOrder"]) -> MetaOapg.properties.stageOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialJobId"]) -> MetaOapg.properties.initialJobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reassignJobId"]) -> MetaOapg.properties.reassignJobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stageOrder", "initialJobId", "reassignJobId", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stageOrder"]) -> MetaOapg.properties.stageOrder: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialJobId"]) -> MetaOapg.properties.initialJobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reassignJobId"]) -> MetaOapg.properties.reassignJobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stageOrder", "initialJobId", "reassignJobId", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        initialJobId: typing.Union[MetaOapg.properties.initialJobId, str, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        stageOrder: typing.Union[MetaOapg.properties.stageOrder, decimal.Decimal, int, ],
        reassignJobId: typing.Union[MetaOapg.properties.reassignJobId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReassignApproverPatchBody':
        return super().__new__(
            cls,
            *args,
            initialJobId=initialJobId,
            message=message,
            stageOrder=stageOrder,
            reassignJobId=reassignJobId,
            _configuration=_configuration,
            **kwargs,
        )
