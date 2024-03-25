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


class CombineScenarioRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "scenarioIds",
        }
        
        class properties:
        
            @staticmethod
            def scenarioIds() -> typing.Type['CombineScenarioRequestScenarioIds']:
                return CombineScenarioRequestScenarioIds
            copyOnly = schemas.BoolSchema
            useScenarioDateForChanges = schemas.BoolSchema
            __annotations__ = {
                "scenarioIds": scenarioIds,
                "copyOnly": copyOnly,
                "useScenarioDateForChanges": useScenarioDateForChanges,
            }
    
    scenarioIds: 'CombineScenarioRequestScenarioIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenarioIds"]) -> 'CombineScenarioRequestScenarioIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyOnly"]) -> MetaOapg.properties.copyOnly: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useScenarioDateForChanges"]) -> MetaOapg.properties.useScenarioDateForChanges: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scenarioIds", "copyOnly", "useScenarioDateForChanges", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenarioIds"]) -> 'CombineScenarioRequestScenarioIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyOnly"]) -> typing.Union[MetaOapg.properties.copyOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useScenarioDateForChanges"]) -> typing.Union[MetaOapg.properties.useScenarioDateForChanges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scenarioIds", "copyOnly", "useScenarioDateForChanges", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scenarioIds: 'CombineScenarioRequestScenarioIds',
        copyOnly: typing.Union[MetaOapg.properties.copyOnly, bool, schemas.Unset] = schemas.unset,
        useScenarioDateForChanges: typing.Union[MetaOapg.properties.useScenarioDateForChanges, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CombineScenarioRequest':
        return super().__new__(
            cls,
            *args,
            scenarioIds=scenarioIds,
            copyOnly=copyOnly,
            useScenarioDateForChanges=useScenarioDateForChanges,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.combine_scenario_request_scenario_ids import CombineScenarioRequestScenarioIds
