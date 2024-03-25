# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_stripe_setup_intent.post import CreateSetupIntentSecretRaw
from chart_hop_python_sdk.paths.v1_stripe_plan.get import GetAllPlansRaw
from chart_hop_python_sdk.paths.v1_stripe_product.get import GetAllProductsRaw
from chart_hop_python_sdk.paths.v1_stripe_product_product_id.get import GetProductByIdRaw
from chart_hop_python_sdk.paths.v1_stripe_webhook.post import ProcessWebhookEventsRaw


class StripeApiRaw(
    CreateSetupIntentSecretRaw,
    GetAllPlansRaw,
    GetAllProductsRaw,
    GetProductByIdRaw,
    ProcessWebhookEventsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass