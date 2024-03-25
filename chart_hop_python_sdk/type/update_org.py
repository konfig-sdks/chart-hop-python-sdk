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

from chart_hop_python_sdk.type.address import Address
from chart_hop_python_sdk.type.onboard_step_result import OnboardStepResult
from chart_hop_python_sdk.type.org_domain import OrgDomain
from chart_hop_python_sdk.type.update_org_currencies import UpdateOrgCurrencies

class RequiredUpdateOrg(TypedDict):
    pass

class OptionalUpdateOrg(TypedDict, total=False):
    # customer for billing processing
    customerId: str

    # name of organization
    name: str

    # unique slug of organization
    slug: str

    # type of organization
    type: str

    # industry
    industry: str

    # approximate number of employees
    estEmployees: int

    # approximate amount of revenue
    estRevenue: int

    # year of founding
    foundedYear: int

    address: Address

    # company phone number in E.164 format
    phone: str

    # primary contact email
    email: str

    # website URL
    url: str

    # domains used by this org
    domains: typing.List[OrgDomain]

    # current status of organization
    status: str

    # path to full-sized profile image in storage
    imagePath: str

    currencies: UpdateOrgCurrencies

    # stock symbol
    stock: str

    # timezone in use
    timezone: str

    # approximate time of day for daily app syncs to run (defaults to 9am Eastern time)
    appTime: str

    # infrastructure zone
    zone: int

    # number of months into the calendar year that the fiscal year starts (1 = February, 2 = March)
    fiscalStart: int

    # start date of history
    startDate: str

    # map of sensitive field defaults
    sensitiveFields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # org-public options
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # internal (ChartHop controlled) options
    internalOptions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # list of onboard steps that this Org has completed (or skipped)
    onboardSteps: typing.List[OnboardStepResult]

    # current onboarding status of an organization, allowing clearing of org
    onboarding: bool

    # completion status of initial import for orgs signed up via self serve
    selfServeImporting: bool

    # number of total headcount currently in the org
    headCount: int

class UpdateOrg(RequiredUpdateOrg, OptionalUpdateOrg):
    pass
