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


class CreateProduct(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "features",
            "stripeProductId",
            "salesforceProductId",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            salesforceProductId = schemas.StrSchema
            stripeProductId = schemas.StrSchema
        
            @staticmethod
            def features() -> typing.Type['CreateProductFeatures']:
                return CreateProductFeatures
            sku = schemas.StrSchema
        
            @staticmethod
            def featureOptions() -> typing.Type['CreateProductFeatureOptions']:
                return CreateProductFeatureOptions
            __annotations__ = {
                "name": name,
                "salesforceProductId": salesforceProductId,
                "stripeProductId": stripeProductId,
                "features": features,
                "sku": sku,
                "featureOptions": featureOptions,
            }
    
    features: 'CreateProductFeatures'
    stripeProductId: MetaOapg.properties.stripeProductId
    salesforceProductId: MetaOapg.properties.salesforceProductId
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salesforceProductId"]) -> MetaOapg.properties.salesforceProductId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripeProductId"]) -> MetaOapg.properties.stripeProductId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> 'CreateProductFeatures': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sku"]) -> MetaOapg.properties.sku: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featureOptions"]) -> 'CreateProductFeatureOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "salesforceProductId", "stripeProductId", "features", "sku", "featureOptions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salesforceProductId"]) -> MetaOapg.properties.salesforceProductId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripeProductId"]) -> MetaOapg.properties.stripeProductId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> 'CreateProductFeatures': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sku"]) -> typing.Union[MetaOapg.properties.sku, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featureOptions"]) -> typing.Union['CreateProductFeatureOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "salesforceProductId", "stripeProductId", "features", "sku", "featureOptions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        features: 'CreateProductFeatures',
        stripeProductId: typing.Union[MetaOapg.properties.stripeProductId, str, ],
        salesforceProductId: typing.Union[MetaOapg.properties.salesforceProductId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        sku: typing.Union[MetaOapg.properties.sku, str, schemas.Unset] = schemas.unset,
        featureOptions: typing.Union['CreateProductFeatureOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateProduct':
        return super().__new__(
            cls,
            *args,
            features=features,
            stripeProductId=stripeProductId,
            salesforceProductId=salesforceProductId,
            name=name,
            sku=sku,
            featureOptions=featureOptions,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.create_product_feature_options import CreateProductFeatureOptions
from chart_hop_python_sdk.model.create_product_features import CreateProductFeatures
