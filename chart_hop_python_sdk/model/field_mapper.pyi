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


class FieldMapper(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "remoteFields",
            "charthopFields",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def charthopFields() -> typing.Type['FieldMapperCharthopFields']:
                return FieldMapperCharthopFields
        
            @staticmethod
            def remoteFields() -> typing.Type['FieldMapperRemoteFields']:
                return FieldMapperRemoteFields
            type = schemas.StrSchema
            id = schemas.StrSchema
            defaultCharthopValue = schemas.StrSchema
            defaultRemoteValue = schemas.StrSchema
            defaultAmount = schemas.NumberSchema
            defaultCurrency = schemas.StrSchema
            transformFunction = schemas.StrSchema
            charthopToRemoteTransformFunction = schemas.StrSchema
        
            @staticmethod
            def map() -> typing.Type['FieldMapperMap']:
                return FieldMapperMap
        
            @staticmethod
            def charthopToRemoteMap() -> typing.Type['FieldMapperCharthopToRemoteMap']:
                return FieldMapperCharthopToRemoteMap
            idField = schemas.StrSchema
            nameField = schemas.StrSchema
            remoteToCharthopMultiplier = schemas.NumberSchema
            __annotations__ = {
                "charthopFields": charthopFields,
                "remoteFields": remoteFields,
                "type": type,
                "id": id,
                "defaultCharthopValue": defaultCharthopValue,
                "defaultRemoteValue": defaultRemoteValue,
                "defaultAmount": defaultAmount,
                "defaultCurrency": defaultCurrency,
                "transformFunction": transformFunction,
                "charthopToRemoteTransformFunction": charthopToRemoteTransformFunction,
                "map": map,
                "charthopToRemoteMap": charthopToRemoteMap,
                "idField": idField,
                "nameField": nameField,
                "remoteToCharthopMultiplier": remoteToCharthopMultiplier,
            }
    
    remoteFields: 'FieldMapperRemoteFields'
    charthopFields: 'FieldMapperCharthopFields'
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["charthopFields"]) -> 'FieldMapperCharthopFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remoteFields"]) -> 'FieldMapperRemoteFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultCharthopValue"]) -> MetaOapg.properties.defaultCharthopValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultRemoteValue"]) -> MetaOapg.properties.defaultRemoteValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultAmount"]) -> MetaOapg.properties.defaultAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultCurrency"]) -> MetaOapg.properties.defaultCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transformFunction"]) -> MetaOapg.properties.transformFunction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["charthopToRemoteTransformFunction"]) -> MetaOapg.properties.charthopToRemoteTransformFunction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map"]) -> 'FieldMapperMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["charthopToRemoteMap"]) -> 'FieldMapperCharthopToRemoteMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idField"]) -> MetaOapg.properties.idField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameField"]) -> MetaOapg.properties.nameField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remoteToCharthopMultiplier"]) -> MetaOapg.properties.remoteToCharthopMultiplier: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["charthopFields", "remoteFields", "type", "id", "defaultCharthopValue", "defaultRemoteValue", "defaultAmount", "defaultCurrency", "transformFunction", "charthopToRemoteTransformFunction", "map", "charthopToRemoteMap", "idField", "nameField", "remoteToCharthopMultiplier", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["charthopFields"]) -> 'FieldMapperCharthopFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remoteFields"]) -> 'FieldMapperRemoteFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultCharthopValue"]) -> typing.Union[MetaOapg.properties.defaultCharthopValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultRemoteValue"]) -> typing.Union[MetaOapg.properties.defaultRemoteValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultAmount"]) -> typing.Union[MetaOapg.properties.defaultAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultCurrency"]) -> typing.Union[MetaOapg.properties.defaultCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transformFunction"]) -> typing.Union[MetaOapg.properties.transformFunction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["charthopToRemoteTransformFunction"]) -> typing.Union[MetaOapg.properties.charthopToRemoteTransformFunction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map"]) -> typing.Union['FieldMapperMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["charthopToRemoteMap"]) -> typing.Union['FieldMapperCharthopToRemoteMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idField"]) -> typing.Union[MetaOapg.properties.idField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameField"]) -> typing.Union[MetaOapg.properties.nameField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remoteToCharthopMultiplier"]) -> typing.Union[MetaOapg.properties.remoteToCharthopMultiplier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["charthopFields", "remoteFields", "type", "id", "defaultCharthopValue", "defaultRemoteValue", "defaultAmount", "defaultCurrency", "transformFunction", "charthopToRemoteTransformFunction", "map", "charthopToRemoteMap", "idField", "nameField", "remoteToCharthopMultiplier", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        remoteFields: 'FieldMapperRemoteFields',
        charthopFields: 'FieldMapperCharthopFields',
        type: typing.Union[MetaOapg.properties.type, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        defaultCharthopValue: typing.Union[MetaOapg.properties.defaultCharthopValue, str, schemas.Unset] = schemas.unset,
        defaultRemoteValue: typing.Union[MetaOapg.properties.defaultRemoteValue, str, schemas.Unset] = schemas.unset,
        defaultAmount: typing.Union[MetaOapg.properties.defaultAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        defaultCurrency: typing.Union[MetaOapg.properties.defaultCurrency, str, schemas.Unset] = schemas.unset,
        transformFunction: typing.Union[MetaOapg.properties.transformFunction, str, schemas.Unset] = schemas.unset,
        charthopToRemoteTransformFunction: typing.Union[MetaOapg.properties.charthopToRemoteTransformFunction, str, schemas.Unset] = schemas.unset,
        map: typing.Union['FieldMapperMap', schemas.Unset] = schemas.unset,
        charthopToRemoteMap: typing.Union['FieldMapperCharthopToRemoteMap', schemas.Unset] = schemas.unset,
        idField: typing.Union[MetaOapg.properties.idField, str, schemas.Unset] = schemas.unset,
        nameField: typing.Union[MetaOapg.properties.nameField, str, schemas.Unset] = schemas.unset,
        remoteToCharthopMultiplier: typing.Union[MetaOapg.properties.remoteToCharthopMultiplier, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldMapper':
        return super().__new__(
            cls,
            *args,
            remoteFields=remoteFields,
            charthopFields=charthopFields,
            type=type,
            id=id,
            defaultCharthopValue=defaultCharthopValue,
            defaultRemoteValue=defaultRemoteValue,
            defaultAmount=defaultAmount,
            defaultCurrency=defaultCurrency,
            transformFunction=transformFunction,
            charthopToRemoteTransformFunction=charthopToRemoteTransformFunction,
            map=map,
            charthopToRemoteMap=charthopToRemoteMap,
            idField=idField,
            nameField=nameField,
            remoteToCharthopMultiplier=remoteToCharthopMultiplier,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.field_mapper_charthop_fields import FieldMapperCharthopFields
from chart_hop_python_sdk.model.field_mapper_charthop_to_remote_map import FieldMapperCharthopToRemoteMap
from chart_hop_python_sdk.model.field_mapper_map import FieldMapperMap
from chart_hop_python_sdk.model.field_mapper_remote_fields import FieldMapperRemoteFields
