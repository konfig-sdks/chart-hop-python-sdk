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

from chart_hop_python_sdk.type.category import Category
from chart_hop_python_sdk.type.category_sort import CategorySort
from chart_hop_python_sdk.type.comp_band import CompBand
from chart_hop_python_sdk.type.customer import Customer
from chart_hop_python_sdk.type.customer_details import CustomerDetails
from chart_hop_python_sdk.type.exchange_rate import ExchangeRate
from chart_hop_python_sdk.type.feature_access_option import FeatureAccessOption
from chart_hop_python_sdk.type.field import Field
from chart_hop_python_sdk.type.form import Form
from chart_hop_python_sdk.type.job import Job
from chart_hop_python_sdk.type.org import Org
from chart_hop_python_sdk.type.org_config import OrgConfig
from chart_hop_python_sdk.type.org_stock_data import OrgStockData
from chart_hop_python_sdk.type.person import Person
from chart_hop_python_sdk.type.preload_response_feature_access import PreloadResponseFeatureAccess
from chart_hop_python_sdk.type.preload_response_groups import PreloadResponseGroups
from chart_hop_python_sdk.type.preload_response_jobs import PreloadResponseJobs
from chart_hop_python_sdk.type.preload_response_ui_access import PreloadResponseUiAccess
from chart_hop_python_sdk.type.question import Question
from chart_hop_python_sdk.type.role import Role
from chart_hop_python_sdk.type.scenario import Scenario
from chart_hop_python_sdk.type.user import User

class RequiredPreloadResponse(TypedDict):
    org: Org

    orgs: typing.List[Org]

    user: User

    groups: PreloadResponseGroups

    scenarios: typing.List[Scenario]

    users: typing.List[User]

    fields: typing.List[Field]

    forms: typing.List[Form]

    featureAccess: PreloadResponseFeatureAccess

    categories: typing.List[Category]

    jobs: PreloadResponseJobs

    persons: typing.List[Person]

    compBands: typing.List[CompBand]

    questions: typing.List[Question]

class OptionalPreloadResponse(TypedDict, total=False):
    role: Role

    viewUser: User

    viewRole: Role

    exchangeRate: ExchangeRate

    stock: OrgStockData

    job: Job

    customer: Customer

    customerDetails: CustomerDetails

    enabledFeatureOptions: typing.List[FeatureAccessOption]

    categorySort: CategorySort

    orgConfig: OrgConfig

    uiAccess: PreloadResponseUiAccess

class PreloadResponse(RequiredPreloadResponse, OptionalPreloadResponse):
    pass
