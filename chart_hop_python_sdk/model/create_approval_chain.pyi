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


class CreateApprovalChain(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "approvalNotifierUserIds",
            "isPreview",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            isPreview = schemas.BoolSchema
        
            @staticmethod
            def approvalNotifierUserIds() -> typing.Type['CreateApprovalChainApprovalNotifierUserIds']:
                return CreateApprovalChainApprovalNotifierUserIds
            entityId = schemas.StrSchema
            
            
            class entityType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMP_REVIEW(cls):
                    return cls("COMP_REVIEW")
                
                @schemas.classproperty
                def SCENARIO(cls):
                    return cls("SCENARIO")
                
                @schemas.classproperty
                def TIMEOFF(cls):
                    return cls("TIMEOFF")
            fallbackApproverJobId = schemas.StrSchema
            fallbackApproverJobError = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "isPreview": isPreview,
                "approvalNotifierUserIds": approvalNotifierUserIds,
                "entityId": entityId,
                "entityType": entityType,
                "fallbackApproverJobId": fallbackApproverJobId,
                "fallbackApproverJobError": fallbackApproverJobError,
            }
    
    approvalNotifierUserIds: 'CreateApprovalChainApprovalNotifierUserIds'
    isPreview: MetaOapg.properties.isPreview
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPreview"]) -> MetaOapg.properties.isPreview: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalNotifierUserIds"]) -> 'CreateApprovalChainApprovalNotifierUserIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityType"]) -> MetaOapg.properties.entityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fallbackApproverJobId"]) -> MetaOapg.properties.fallbackApproverJobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fallbackApproverJobError"]) -> MetaOapg.properties.fallbackApproverJobError: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "isPreview", "approvalNotifierUserIds", "entityId", "entityType", "fallbackApproverJobId", "fallbackApproverJobError", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPreview"]) -> MetaOapg.properties.isPreview: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalNotifierUserIds"]) -> 'CreateApprovalChainApprovalNotifierUserIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityId"]) -> typing.Union[MetaOapg.properties.entityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityType"]) -> typing.Union[MetaOapg.properties.entityType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fallbackApproverJobId"]) -> typing.Union[MetaOapg.properties.fallbackApproverJobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fallbackApproverJobError"]) -> typing.Union[MetaOapg.properties.fallbackApproverJobError, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "isPreview", "approvalNotifierUserIds", "entityId", "entityType", "fallbackApproverJobId", "fallbackApproverJobError", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        approvalNotifierUserIds: 'CreateApprovalChainApprovalNotifierUserIds',
        isPreview: typing.Union[MetaOapg.properties.isPreview, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        entityId: typing.Union[MetaOapg.properties.entityId, str, schemas.Unset] = schemas.unset,
        entityType: typing.Union[MetaOapg.properties.entityType, str, schemas.Unset] = schemas.unset,
        fallbackApproverJobId: typing.Union[MetaOapg.properties.fallbackApproverJobId, str, schemas.Unset] = schemas.unset,
        fallbackApproverJobError: typing.Union[MetaOapg.properties.fallbackApproverJobError, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateApprovalChain':
        return super().__new__(
            cls,
            *args,
            approvalNotifierUserIds=approvalNotifierUserIds,
            isPreview=isPreview,
            name=name,
            entityId=entityId,
            entityType=entityType,
            fallbackApproverJobId=fallbackApproverJobId,
            fallbackApproverJobError=fallbackApproverJobError,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.create_approval_chain_approval_notifier_user_ids import CreateApprovalChainApprovalNotifierUserIds