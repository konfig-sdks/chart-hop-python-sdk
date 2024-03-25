# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_stripe_setup_intent.post import CreateSetupIntentSecret
from chart_hop_python_sdk.paths.v1_stripe_plan.get import GetAllPlans
from chart_hop_python_sdk.paths.v1_stripe_product.get import GetAllProducts
from chart_hop_python_sdk.paths.v1_stripe_product_product_id.get import GetProductById
from chart_hop_python_sdk.paths.v1_stripe_webhook.post import ProcessWebhookEvents
from chart_hop_python_sdk.apis.tags.stripe_api_raw import StripeApiRaw


class StripeApi(
    CreateSetupIntentSecret,
    GetAllPlans,
    GetAllProducts,
    GetProductById,
    ProcessWebhookEvents,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: StripeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = StripeApiRaw(api_client)