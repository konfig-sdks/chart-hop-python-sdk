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


class TiersResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "reviews",
            "finalApprovers",
        }
        
        class properties:
        
            @staticmethod
            def reviews() -> typing.Type['TiersResponseReviews']:
                return TiersResponseReviews
        
            @staticmethod
            def finalApprovers() -> typing.Type['TiersResponseFinalApprovers']:
                return TiersResponseFinalApprovers
            __annotations__ = {
                "reviews": reviews,
                "finalApprovers": finalApprovers,
            }
    
    reviews: 'TiersResponseReviews'
    finalApprovers: 'TiersResponseFinalApprovers'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviews"]) -> 'TiersResponseReviews': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finalApprovers"]) -> 'TiersResponseFinalApprovers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["reviews", "finalApprovers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviews"]) -> 'TiersResponseReviews': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finalApprovers"]) -> 'TiersResponseFinalApprovers': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reviews", "finalApprovers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        reviews: 'TiersResponseReviews',
        finalApprovers: 'TiersResponseFinalApprovers',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TiersResponse':
        return super().__new__(
            cls,
            *args,
            reviews=reviews,
            finalApprovers=finalApprovers,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.tiers_response_final_approvers import TiersResponseFinalApprovers
from chart_hop_python_sdk.model.tiers_response_reviews import TiersResponseReviews