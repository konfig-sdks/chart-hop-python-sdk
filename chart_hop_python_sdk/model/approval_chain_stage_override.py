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


class ApprovalChainStageOverride(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "approvalChainStageId",
            "order",
            "stageOverrideId",
            "status",
        }
        
        class properties:
            stageOverrideId = schemas.StrSchema
            approvalChainStageId = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "CANCELED": "CANCELED",
                        "REJECTED": "REJECTED",
                        "PENDING": "PENDING",
                        "ACTIVE": "ACTIVE",
                        "REVIEWED": "REVIEWED",
                        "APPROVED": "APPROVED",
                        "SKIPPED": "SKIPPED",
                        "SUBMITTED": "SUBMITTED",
                    }
                
                @schemas.classproperty
                def CANCELED(cls):
                    return cls("CANCELED")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("REJECTED")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def REVIEWED(cls):
                    return cls("REVIEWED")
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("APPROVED")
                
                @schemas.classproperty
                def SKIPPED(cls):
                    return cls("SKIPPED")
                
                @schemas.classproperty
                def SUBMITTED(cls):
                    return cls("SUBMITTED")
            order = schemas.Int32Schema
            
            
            class groups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApprovalGroup']:
                        return ApprovalGroup
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ApprovalGroup'], typing.List['ApprovalGroup']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groups':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApprovalGroup':
                    return super().__getitem__(i)
            __annotations__ = {
                "stageOverrideId": stageOverrideId,
                "approvalChainStageId": approvalChainStageId,
                "status": status,
                "order": order,
                "groups": groups,
            }
    
    approvalChainStageId: MetaOapg.properties.approvalChainStageId
    order: MetaOapg.properties.order
    stageOverrideId: MetaOapg.properties.stageOverrideId
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stageOverrideId"]) -> MetaOapg.properties.stageOverrideId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalChainStageId"]) -> MetaOapg.properties.approvalChainStageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> MetaOapg.properties.groups: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stageOverrideId", "approvalChainStageId", "status", "order", "groups", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stageOverrideId"]) -> MetaOapg.properties.stageOverrideId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalChainStageId"]) -> MetaOapg.properties.approvalChainStageId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union[MetaOapg.properties.groups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stageOverrideId", "approvalChainStageId", "status", "order", "groups", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        approvalChainStageId: typing.Union[MetaOapg.properties.approvalChainStageId, str, ],
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, ],
        stageOverrideId: typing.Union[MetaOapg.properties.stageOverrideId, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        groups: typing.Union[MetaOapg.properties.groups, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApprovalChainStageOverride':
        return super().__new__(
            cls,
            *args,
            approvalChainStageId=approvalChainStageId,
            order=order,
            stageOverrideId=stageOverrideId,
            status=status,
            groups=groups,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.approval_group import ApprovalGroup
