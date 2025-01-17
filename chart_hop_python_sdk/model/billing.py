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


class Billing(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "invoices",
            "org",
            "customer",
        }
        
        class properties:
        
            @staticmethod
            def customer() -> typing.Type['Customer']:
                return Customer
            
            
            class invoices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Invoice']:
                        return Invoice
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Invoice'], typing.List['Invoice']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'invoices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Invoice':
                    return super().__getitem__(i)
        
            @staticmethod
            def org() -> typing.Type['Org']:
                return Org
        
            @staticmethod
            def checkout() -> typing.Type['Checkout']:
                return Checkout
        
            @staticmethod
            def paymentInfo() -> typing.Type['PaymentInfo']:
                return PaymentInfo
        
            @staticmethod
            def plan() -> typing.Type['Plan']:
                return Plan
            __annotations__ = {
                "customer": customer,
                "invoices": invoices,
                "org": org,
                "checkout": checkout,
                "paymentInfo": paymentInfo,
                "plan": plan,
            }
    
    invoices: MetaOapg.properties.invoices
    org: 'Org'
    customer: 'Customer'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoices"]) -> MetaOapg.properties.invoices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org"]) -> 'Org': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkout"]) -> 'Checkout': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentInfo"]) -> 'PaymentInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan"]) -> 'Plan': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer", "invoices", "org", "checkout", "paymentInfo", "plan", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoices"]) -> MetaOapg.properties.invoices: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org"]) -> 'Org': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkout"]) -> typing.Union['Checkout', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentInfo"]) -> typing.Union['PaymentInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> typing.Union['Plan', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer", "invoices", "org", "checkout", "paymentInfo", "plan", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        invoices: typing.Union[MetaOapg.properties.invoices, list, tuple, ],
        org: 'Org',
        customer: 'Customer',
        checkout: typing.Union['Checkout', schemas.Unset] = schemas.unset,
        paymentInfo: typing.Union['PaymentInfo', schemas.Unset] = schemas.unset,
        plan: typing.Union['Plan', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Billing':
        return super().__new__(
            cls,
            *args,
            invoices=invoices,
            org=org,
            customer=customer,
            checkout=checkout,
            paymentInfo=paymentInfo,
            plan=plan,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.checkout import Checkout
from chart_hop_python_sdk.model.customer import Customer
from chart_hop_python_sdk.model.invoice import Invoice
from chart_hop_python_sdk.model.org import Org
from chart_hop_python_sdk.model.payment_info import PaymentInfo
from chart_hop_python_sdk.model.plan import Plan
