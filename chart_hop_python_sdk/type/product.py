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

from chart_hop_python_sdk.type.product_feature_options import ProductFeatureOptions
from chart_hop_python_sdk.type.product_features import ProductFeatures

class RequiredProduct(TypedDict):
    # name of product
    name: str

    # unique sku of product
    sku: str

    # corresponding product id in salesforce
    salesforceProductId: str

    # corresponding product id in stripe
    stripeProductId: str

    features: ProductFeatures

class OptionalProduct(TypedDict, total=False):
    # globally unique id
    id: str

    featureOptions: ProductFeatureOptions

class Product(RequiredProduct, OptionalProduct):
    pass
