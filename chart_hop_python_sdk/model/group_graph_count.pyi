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


class GroupGraphCount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "groupCount",
            "jobCount",
            "personCount",
        }
        
        class properties:
            jobCount = schemas.NumberSchema
            personCount = schemas.NumberSchema
            groupCount = schemas.NumberSchema
            __annotations__ = {
                "jobCount": jobCount,
                "personCount": personCount,
                "groupCount": groupCount,
            }
    
    groupCount: MetaOapg.properties.groupCount
    jobCount: MetaOapg.properties.jobCount
    personCount: MetaOapg.properties.personCount
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobCount"]) -> MetaOapg.properties.jobCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personCount"]) -> MetaOapg.properties.personCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupCount"]) -> MetaOapg.properties.groupCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobCount", "personCount", "groupCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobCount"]) -> MetaOapg.properties.jobCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personCount"]) -> MetaOapg.properties.personCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupCount"]) -> MetaOapg.properties.groupCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobCount", "personCount", "groupCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        groupCount: typing.Union[MetaOapg.properties.groupCount, decimal.Decimal, int, float, ],
        jobCount: typing.Union[MetaOapg.properties.jobCount, decimal.Decimal, int, float, ],
        personCount: typing.Union[MetaOapg.properties.personCount, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupGraphCount':
        return super().__new__(
            cls,
            *args,
            groupCount=groupCount,
            jobCount=jobCount,
            personCount=personCount,
            _configuration=_configuration,
            **kwargs,
        )
