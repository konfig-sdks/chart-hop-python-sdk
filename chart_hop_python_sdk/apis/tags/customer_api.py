# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_customer.post import CreateNewCustomer
from chart_hop_python_sdk.paths.v1_customer_customer_id_invoices.get import GetAllInvoicesForCustomer
from chart_hop_python_sdk.paths.v1_customer_customer_id.get import GetById
from chart_hop_python_sdk.paths.v1_customer_customer_id_subscription.get import GetCharthopSubscription
from chart_hop_python_sdk.paths.v1_customer.get import ListVisibleCustomers
from chart_hop_python_sdk.paths.v1_customer_customer_id.patch import UpdateExistingCustomer
from chart_hop_python_sdk.paths.v1_customer_customer_id_subscription.patch import UpdateSubscription
from chart_hop_python_sdk.apis.tags.customer_api_raw import CustomerApiRaw


class CustomerApi(
    CreateNewCustomer,
    GetAllInvoicesForCustomer,
    GetById,
    GetCharthopSubscription,
    ListVisibleCustomers,
    UpdateExistingCustomer,
    UpdateSubscription,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CustomerApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CustomerApiRaw(api_client)