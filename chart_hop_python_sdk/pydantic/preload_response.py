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

from chart_hop_python_sdk.pydantic.category import Category
from chart_hop_python_sdk.pydantic.category_sort import CategorySort
from chart_hop_python_sdk.pydantic.comp_band import CompBand
from chart_hop_python_sdk.pydantic.customer import Customer
from chart_hop_python_sdk.pydantic.customer_details import CustomerDetails
from chart_hop_python_sdk.pydantic.exchange_rate import ExchangeRate
from chart_hop_python_sdk.pydantic.feature_access_option import FeatureAccessOption
from chart_hop_python_sdk.pydantic.field import Field
from chart_hop_python_sdk.pydantic.form import Form
from chart_hop_python_sdk.pydantic.job import Job
from chart_hop_python_sdk.pydantic.org import Org
from chart_hop_python_sdk.pydantic.org_config import OrgConfig
from chart_hop_python_sdk.pydantic.org_stock_data import OrgStockData
from chart_hop_python_sdk.pydantic.person import Person
from chart_hop_python_sdk.pydantic.preload_response_feature_access import PreloadResponseFeatureAccess
from chart_hop_python_sdk.pydantic.preload_response_groups import PreloadResponseGroups
from chart_hop_python_sdk.pydantic.preload_response_jobs import PreloadResponseJobs
from chart_hop_python_sdk.pydantic.preload_response_ui_access import PreloadResponseUiAccess
from chart_hop_python_sdk.pydantic.question import Question
from chart_hop_python_sdk.pydantic.role import Role
from chart_hop_python_sdk.pydantic.scenario import Scenario
from chart_hop_python_sdk.pydantic.user import User

class PreloadResponse(BaseModel):
    org: Org = Field(alias='org')

    orgs: typing.List[Org] = Field(alias='orgs')

    user: User = Field(alias='user')

    groups: PreloadResponseGroups = Field(alias='groups')

    scenarios: typing.List[Scenario] = Field(alias='scenarios')

    users: typing.List[User] = Field(alias='users')

    fields: typing.List[Field] = Field(alias='fields')

    forms: typing.List[Form] = Field(alias='forms')

    feature_access: PreloadResponseFeatureAccess = Field(alias='featureAccess')

    categories: typing.List[Category] = Field(alias='categories')

    jobs: PreloadResponseJobs = Field(alias='jobs')

    persons: typing.List[Person] = Field(alias='persons')

    comp_bands: typing.List[CompBand] = Field(alias='compBands')

    questions: typing.List[Question] = Field(alias='questions')

    role: typing.Optional[Role] = Field(None, alias='role')

    view_user: typing.Optional[User] = Field(None, alias='viewUser')

    view_role: typing.Optional[Role] = Field(None, alias='viewRole')

    exchange_rate: typing.Optional[ExchangeRate] = Field(None, alias='exchangeRate')

    stock: typing.Optional[OrgStockData] = Field(None, alias='stock')

    job: typing.Optional[Job] = Field(None, alias='job')

    customer: typing.Optional[Customer] = Field(None, alias='customer')

    customer_details: typing.Optional[CustomerDetails] = Field(None, alias='customerDetails')

    enabled_feature_options: typing.Optional[typing.List[FeatureAccessOption]] = Field(None, alias='enabledFeatureOptions')

    category_sort: typing.Optional[CategorySort] = Field(None, alias='categorySort')

    org_config: typing.Optional[OrgConfig] = Field(None, alias='orgConfig')

    ui_access: typing.Optional[PreloadResponseUiAccess] = Field(None, alias='uiAccess')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
