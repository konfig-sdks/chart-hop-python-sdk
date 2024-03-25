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

from chart_hop_python_sdk.pydantic.create_product_feature_options import CreateProductFeatureOptions
from chart_hop_python_sdk.pydantic.create_product_features import CreateProductFeatures

class CreateProduct(BaseModel):
    # name of product
    name: str = Field(alias='name')

    # corresponding product id in salesforce
    salesforce_product_id: str = Field(alias='salesforceProductId')

    # corresponding product id in stripe
    stripe_product_id: str = Field(alias='stripeProductId')

    features: CreateProductFeatures = Field(alias='features')

    # unique sku of product
    sku: typing.Optional[str] = Field(None, alias='sku')

    feature_options: typing.Optional[CreateProductFeatureOptions] = Field(None, alias='featureOptions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
