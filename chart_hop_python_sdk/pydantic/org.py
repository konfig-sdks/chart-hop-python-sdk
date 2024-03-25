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

from chart_hop_python_sdk.pydantic.address import Address
from chart_hop_python_sdk.pydantic.onboard_step_result import OnboardStepResult
from chart_hop_python_sdk.pydantic.org_currencies import OrgCurrencies
from chart_hop_python_sdk.pydantic.org_domain import OrgDomain

class Org(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # name of organization
    name: str = Field(alias='name')

    # unique slug of organization
    slug: str = Field(alias='slug')

    # customer for billing processing
    customer_id: typing.Optional[str] = Field(None, alias='customerId')

    # type of organization
    type: typing.Optional[Literal["PRIVATE", "PUBLIC", "EDU", "GOV", "NONPROFIT", "DEMO", "TEST"]] = Field(None, alias='type')

    # industry
    industry: typing.Optional[str] = Field(None, alias='industry')

    # approximate number of employees
    est_employees: typing.Optional[int] = Field(None, alias='estEmployees')

    # approximate amount of revenue
    est_revenue: typing.Optional[int] = Field(None, alias='estRevenue')

    # year of founding
    founded_year: typing.Optional[int] = Field(None, alias='foundedYear')

    address: typing.Optional[Address] = Field(None, alias='address')

    # company phone number in E.164 format
    phone: typing.Optional[str] = Field(None, alias='phone')

    # primary contact email
    email: typing.Optional[str] = Field(None, alias='email')

    # website URL
    url: typing.Optional[str] = Field(None, alias='url')

    # domains used by this org
    domains: typing.Optional[typing.List[OrgDomain]] = Field(None, alias='domains')

    # current status of organization
    status: typing.Optional[Literal["ACTIVE", "INACTIVE", "DISABLED"]] = Field(None, alias='status')

    # path to full-sized profile image in storage
    image_path: typing.Optional[str] = Field(None, alias='imagePath')

    currencies: typing.Optional[OrgCurrencies] = Field(None, alias='currencies')

    # stock symbol
    stock: typing.Optional[str] = Field(None, alias='stock')

    # timezone in use
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # approximate time of day for daily app syncs to run (defaults to 9am Eastern time)
    app_time: typing.Optional[str] = Field(None, alias='appTime')

    # infrastructure zone
    zone: typing.Optional[int] = Field(None, alias='zone')

    # number of months into the calendar year that the fiscal year starts (1 = February, 2 = March)
    fiscal_start: typing.Optional[int] = Field(None, alias='fiscalStart')

    # head of the organization
    head_job_id: typing.Optional[str] = Field(None, alias='headJobId')

    # start date of history
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # map of sensitive field defaults
    sensitive_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='sensitiveFields')

    # org-public options
    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    # internal (ChartHop controlled) options
    internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='internalOptions')

    # list of onboard steps that this Org has completed (or skipped)
    onboard_steps: typing.Optional[typing.List[OnboardStepResult]] = Field(None, alias='onboardSteps')

    # current onboarding status of an organization, allowing clearing of org
    onboarding: typing.Optional[bool] = Field(None, alias='onboarding')

    # completion status of initial import for orgs signed up via self serve
    self_serve_importing: typing.Optional[bool] = Field(None, alias='selfServeImporting')

    # number of total headcount currently in the org
    head_count: typing.Optional[int] = Field(None, alias='headCount')

    # number of non-ChartHop, non-app users in the org
    user_count: typing.Optional[int] = Field(None, alias='userCount')

    # number of non-ChartHop, non-app users in the org active in the past month
    active_user_count: typing.Optional[int] = Field(None, alias='activeUserCount')

    # last timestamp that any user was active in the org
    active_at: typing.Optional[str] = Field(None, alias='activeAt')

    # timestamp of most recent changes made to org
    change_at: typing.Optional[str] = Field(None, alias='changeAt')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # timestamp that the org is marked for data destruction
    destroy_at: typing.Optional[str] = Field(None, alias='destroyAt')

    # user who marked the org for data destruction
    destroy_id: typing.Optional[str] = Field(None, alias='destroyId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )