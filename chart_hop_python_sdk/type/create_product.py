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

from chart_hop_python_sdk.type.create_product_feature_options import CreateProductFeatureOptions
from chart_hop_python_sdk.type.create_product_features import CreateProductFeatures

class RequiredCreateProduct(TypedDict):
    # name of product
    name: str

    # corresponding product id in salesforce
    salesforceProductId: str

    # corresponding product id in stripe
    stripeProductId: str

    features: CreateProductFeatures

class OptionalCreateProduct(TypedDict, total=False):
    # unique sku of product
    sku: str

    featureOptions: CreateProductFeatureOptions

class CreateProduct(RequiredCreateProduct, OptionalCreateProduct):
    pass
