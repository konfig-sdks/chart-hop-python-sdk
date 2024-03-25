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


class Subscription(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "plan",
            "paymentInfo",
            "nextInvoiceAt",
        }
        
        class properties:
            nextInvoiceAt = schemas.StrSchema
        
            @staticmethod
            def plan() -> typing.Type['Plan']:
                return Plan
        
            @staticmethod
            def paymentInfo() -> typing.Type['PaymentInfo']:
                return PaymentInfo
            __annotations__ = {
                "nextInvoiceAt": nextInvoiceAt,
                "plan": plan,
                "paymentInfo": paymentInfo,
            }
    
    plan: 'Plan'
    paymentInfo: 'PaymentInfo'
    nextInvoiceAt: MetaOapg.properties.nextInvoiceAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextInvoiceAt"]) -> MetaOapg.properties.nextInvoiceAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan"]) -> 'Plan': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentInfo"]) -> 'PaymentInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextInvoiceAt", "plan", "paymentInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextInvoiceAt"]) -> MetaOapg.properties.nextInvoiceAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> 'Plan': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentInfo"]) -> 'PaymentInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextInvoiceAt", "plan", "paymentInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        plan: 'Plan',
        paymentInfo: 'PaymentInfo',
        nextInvoiceAt: typing.Union[MetaOapg.properties.nextInvoiceAt, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Subscription':
        return super().__new__(
            cls,
            *args,
            plan=plan,
            paymentInfo=paymentInfo,
            nextInvoiceAt=nextInvoiceAt,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.payment_info import PaymentInfo
from chart_hop_python_sdk.model.plan import Plan