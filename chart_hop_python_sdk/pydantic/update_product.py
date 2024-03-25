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

from chart_hop_python_sdk.pydantic.update_product_feature_options import UpdateProductFeatureOptions
from chart_hop_python_sdk.pydantic.update_product_features import UpdateProductFeatures

class UpdateProduct(BaseModel):
    # name of product
    name: typing.Optional[str] = Field(None, alias='name')

    # unique sku of product
    sku: typing.Optional[str] = Field(None, alias='sku')

    # corresponding product id in salesforce
    salesforce_product_id: typing.Optional[str] = Field(None, alias='salesforceProductId')

    # corresponding product id in stripe
    stripe_product_id: typing.Optional[str] = Field(None, alias='stripeProductId')

    features: typing.Optional[UpdateProductFeatures] = Field(None, alias='features')

    feature_options: typing.Optional[UpdateProductFeatureOptions] = Field(None, alias='featureOptions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
