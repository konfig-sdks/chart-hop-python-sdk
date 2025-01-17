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


class ApprovalGroup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "approvers",
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def REVIEWER(cls):
                    return cls("REVIEWER")
                
                @schemas.classproperty
                def COLLABORATOR(cls):
                    return cls("COLLABORATOR")
                
                @schemas.classproperty
                def FINAL_APPROVER(cls):
                    return cls("FINAL_APPROVER")
            
            
            class approvers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApprovalGroupApprover']:
                        return ApprovalGroupApprover
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ApprovalGroupApprover'], typing.List['ApprovalGroupApprover']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'approvers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApprovalGroupApprover':
                    return super().__getitem__(i)
            groupId = schemas.StrSchema
            expandExpression = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "approvers": approvers,
                "groupId": groupId,
                "expandExpression": expandExpression,
            }
    
    approvers: MetaOapg.properties.approvers
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvers"]) -> MetaOapg.properties.approvers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expandExpression"]) -> MetaOapg.properties.expandExpression: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "approvers", "groupId", "expandExpression", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvers"]) -> MetaOapg.properties.approvers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expandExpression"]) -> typing.Union[MetaOapg.properties.expandExpression, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "approvers", "groupId", "expandExpression", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        approvers: typing.Union[MetaOapg.properties.approvers, list, tuple, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        expandExpression: typing.Union[MetaOapg.properties.expandExpression, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApprovalGroup':
        return super().__new__(
            cls,
            *args,
            approvers=approvers,
            type=type,
            groupId=groupId,
            expandExpression=expandExpression,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.approval_group_approver import ApprovalGroupApprover
