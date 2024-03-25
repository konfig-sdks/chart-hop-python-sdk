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


class TierRepresentationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "eligible",
            "reviewees",
            "reviewer",
        }
        
        class properties:
        
            @staticmethod
            def reviewer() -> typing.Type['Job']:
                return Job
        
            @staticmethod
            def reviewees() -> typing.Type['TierRepresentationResponseReviewees']:
                return TierRepresentationResponseReviewees
            eligible = schemas.BoolSchema
            parentReviewerJobId = schemas.StrSchema
            __annotations__ = {
                "reviewer": reviewer,
                "reviewees": reviewees,
                "eligible": eligible,
                "parentReviewerJobId": parentReviewerJobId,
            }
    
    eligible: MetaOapg.properties.eligible
    reviewees: 'TierRepresentationResponseReviewees'
    reviewer: 'Job'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewer"]) -> 'Job': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewees"]) -> 'TierRepresentationResponseReviewees': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eligible"]) -> MetaOapg.properties.eligible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentReviewerJobId"]) -> MetaOapg.properties.parentReviewerJobId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["reviewer", "reviewees", "eligible", "parentReviewerJobId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewer"]) -> 'Job': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewees"]) -> 'TierRepresentationResponseReviewees': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eligible"]) -> MetaOapg.properties.eligible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentReviewerJobId"]) -> typing.Union[MetaOapg.properties.parentReviewerJobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reviewer", "reviewees", "eligible", "parentReviewerJobId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        eligible: typing.Union[MetaOapg.properties.eligible, bool, ],
        reviewees: 'TierRepresentationResponseReviewees',
        reviewer: 'Job',
        parentReviewerJobId: typing.Union[MetaOapg.properties.parentReviewerJobId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TierRepresentationResponse':
        return super().__new__(
            cls,
            *args,
            eligible=eligible,
            reviewees=reviewees,
            reviewer=reviewer,
            parentReviewerJobId=parentReviewerJobId,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.job import Job
from chart_hop_python_sdk.model.tier_representation_response_reviewees import TierRepresentationResponseReviewees