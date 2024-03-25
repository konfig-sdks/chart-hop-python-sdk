# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.product_feature_options import ProductFeatureOptions
from chart_hop_python_sdk.pydantic.product_features import ProductFeatures

class Product(BaseModel):
    # name of product
    name: str = Field(alias='name')

    # unique sku of product
    sku: str = Field(alias='sku')

    # corresponding product id in salesforce
    salesforce_product_id: str = Field(alias='salesforceProductId')

    # corresponding product id in stripe
    stripe_product_id: str = Field(alias='stripeProductId')

    features: ProductFeatures = Field(alias='features')

    # globally unique id
    id: typing.Optional[str] = Field(None, alias='id')

    feature_options: typing.Optional[ProductFeatureOptions] = Field(None, alias='featureOptions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
