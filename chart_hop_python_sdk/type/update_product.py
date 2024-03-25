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

from chart_hop_python_sdk.type.update_product_feature_options import UpdateProductFeatureOptions
from chart_hop_python_sdk.type.update_product_features import UpdateProductFeatures

class RequiredUpdateProduct(TypedDict):
    pass

class OptionalUpdateProduct(TypedDict, total=False):
    # name of product
    name: str

    # unique sku of product
    sku: str

    # corresponding product id in salesforce
    salesforceProductId: str

    # corresponding product id in stripe
    stripeProductId: str

    features: UpdateProductFeatures

    featureOptions: UpdateProductFeatureOptions

class UpdateProduct(RequiredUpdateProduct, OptionalUpdateProduct):
    pass
