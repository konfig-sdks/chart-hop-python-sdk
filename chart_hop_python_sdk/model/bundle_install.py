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


class BundleInstall(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entities",
        }
        
        class properties:
            
            
            class entities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BundleInstallEntity']:
                        return BundleInstallEntity
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BundleInstallEntity'], typing.List['BundleInstallEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BundleInstallEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "entities": entities,
            }
    
    entities: MetaOapg.properties.entities
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities"]) -> MetaOapg.properties.entities: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["entities", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities"]) -> MetaOapg.properties.entities: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["entities", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entities: typing.Union[MetaOapg.properties.entities, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BundleInstall':
        return super().__new__(
            cls,
            *args,
            entities=entities,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.bundle_install_entity import BundleInstallEntity